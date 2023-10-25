from django.contrib import admin
from .models import ProviderType, Provider


admin.site.register(Provider)
admin.site.register(ProviderType)
