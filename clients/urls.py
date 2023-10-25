from django.urls import path, include
from rest_framework import routers
from .views import ClientView, ClientTypeView

router = routers.DefaultRouter()
router.register(r'clients', ClientView, 'clients')
router.register(r'client-types', ClientTypeView, 'client-types')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
