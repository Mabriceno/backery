from django.urls import path, include
from rest_framework import routers
from .views import DteTypeView

router = routers.DefaultRouter()
router.register(r'dte-types', DteTypeView, 'dte-types')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

