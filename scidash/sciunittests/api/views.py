from random import getrandbits as grb
import json
from datetime import date

from rest_framework import permissions, viewsets
from rest_framework import views, response, mixins

from scidash.sciunittests.filters import (
    ScoreFilter, TestInstanceFilter, TestSuiteFilter
)
from scidash.sciunittests.models import (
    ScoreClass, ScoreInstance, TestClass, TestInstance, TestSuite
)
from scidash.sciunittests.serializers import (
    ScoreClassSerializer, ScoreInstanceSerializer, TestClassSerializer,
    TestInstanceSerializer, TestSuiteSerializer
)


class ScoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScoreInstance.objects.all()
    serializer_class = ScoreInstanceSerializer
    permission_classes = (permissions.AllowAny, )
    filter_class = ScoreFilter


class TestInstanceViewSet(viewsets.ModelViewSet):
    queryset = TestInstance.objects.all()
    serializer_class = TestInstanceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filter_class = TestInstanceFilter


class TestSuiteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteSerializer
    permission_classes = (permissions.AllowAny, )
    filter_class = TestSuiteFilter


class TestClassViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TestClass.objects.all()
    serializer_class = TestClassSerializer
    permission_classes = (permissions.AllowAny, )
    filter_fields = ('class_name', )


class ScoreClassViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScoreClass.objects.all()
    serializer_class = ScoreClassSerializer
    permission_classes = (permissions.AllowAny, )
    filter_fields = ('class_name', )


class TestInstanceCloneView(views.APIView):

    def get(self, request, test_id):
        test_pk = test_id

        try:
            test_instance = TestInstance.objects.get(pk=test_pk)
        except TestInstance.DoesNotExists:
            return response.Response(json.dumps({
                'success': False,
                'message': 'Test Instance not found'
            }), 404)

        new_test_instance = self.clone_test(test_instance)
        print("new_test_instance is ")
        print(new_test_instance)

        serializer = TestInstanceSerializer(new_test_instance)
        print("serializer is ")
        print(serializer)
        
        return response.Response(serializer.data)

    def clone_test(self, test_instance_model):
        test_instance_model.timestamp = date.today()

        test_instance_model.pk = None
        test_instance_model.hash_id = f"{grb(128)}_{grb(22)}"
        test_instance_model.save()

        return test_instance_model



class TestInstanceEditView(views.APIView, mixins.UpdateModelMixin):

    def update(self, request, test_id):
        test_pk = test_id
        instance = TestInstance.objects.get(pk=test_pk)
        print("The test instance is ")
        print(instance)
        print("request.data.get for name is ")
        print(request.data.get("name"))
        instance.name = request.data.get("name")
        instance.save()

        try:
            error = None
            serializer = TestInstanceSerializer(instance, data=request.data, context={'request': request})
            serializer.is_valid()
            self.perform_update(serializer)
        except Exception as e:
            error = e

        if error is None:
            return response.Response(serializer.data)
        else:
            return response.Response(
                {
                    'failed': True,
                    'message': str(error)
                }, 400
            )


    def put(self, request, test_id):
        return self.update(request, test_id)

