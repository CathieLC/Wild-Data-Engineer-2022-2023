from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from comptes.models import Client

admin.site.register(Client, UserAdmin)

