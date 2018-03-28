from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from general.models import ScidashUser

# Register your models here.

admin.site.register(ScidashUser, UserAdmin)
