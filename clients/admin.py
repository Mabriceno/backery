from django.contrib import admin
from .models import Client, ClientType

admin.site.register(Client)
admin.site.register(ClientType)