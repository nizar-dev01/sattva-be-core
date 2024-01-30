from django.contrib import admin
from core import models

from .user_admin import UserAdmin

admin.site.register(models.User, UserAdmin)
