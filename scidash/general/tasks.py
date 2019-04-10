import json
import os

from celery import shared_task, utils
from django.conf import settings as s

import pygeppetto_gateway as pg
from pygeppetto_server.messages import Servlet as S
from pygeppetto_server.messages import ServletResponse as SR
from scidash.sciunittests.models import ScoreInstance as Score

logger = utils.log.get_task_logger(__name__)


def get_project_id(raw_data):
    data = json.loads(raw_data)
    project_data = json.loads(data.get('project_loaded'))
    logger.info(project_data)

    return project_data.get('project').get('id')


def get_error(raw_data):
    return raw_data


@shared_task
def run_experiment():
    scores = Score.objects.filter(status=Score.SCHEDULED)

    for score in scores:
        logger.info(f'Processing score with ID {score.pk}')
        model_name = os.path.basename(score.model_instance.url)

        project_builder = pg.GeppettoProjectBuilder(
            score=score,
            project_location=f"{s.PYGEPPETTO_BUILDER_PROJECT_BASE_URL}/{score.owner}/{score.pk}/project.json",
            xmi_location=f"{s.PYGEPPETTO_BUILDER_PROJECT_BASE_URL}/{score.owner}/{score.pk}/model.xmi",
            nml_location=f"{s.PYGEPPETTO_BUILDER_PROJECT_BASE_URL}/{score.owner}/{score.pk}/{model_name}",
            )

        project_url = project_builder.build_project()

        servlet_manager = pg.GeppettoServletManager()
        servlet_manager.handle(S.LOAD_PROJECT_FROM_URL, project_url)

        project_loaded = False
        model_loaded = False

        project_id = None

        while not project_loaded and not model_loaded:
            try:
                response = json.loads(servlet_manager.read())
            except Exception as e:
                return e

            response_type = response.get('type')

            logger.info(response_type)

            if response_type == 'generic_error':
                return get_error(response.get('data'))

            project_loaded = response_type == SR.PROJECT_LOADED
            model_loaded = response_type == SR.GEPPETTO_MODEL_LOADED

            if project_loaded:
                project_id = get_project_id(response.get('data'))
                logger.info(project_id)

        if project_id is None:
            return "Project not found"

        score.status = Score.LOCKED
        score.save()

        servlet_manager.handle(
            S.RUN_EXPERIMENT,
            json.dumps({
                'projectId': project_id,
                'experimentId': 1
            })
        )
