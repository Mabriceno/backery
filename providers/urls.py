from django.urls import path, include
from rest_framework import routers
from .views import ProviderView, ProviderTypeView

router = routers.DefaultRouter()
router.register(r'providers', ProviderView, 'providers')
router.register(r'provider-types', ProviderTypeView, 'provider-types')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]