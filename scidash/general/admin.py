from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.models import ContentType

from scidash.general.models import ScidashUser, Tag

# Register your models here.

admin.site.register(ScidashUser, UserAdmin)
admin.site.register(ContentType)
admin.site.register(Tag)
