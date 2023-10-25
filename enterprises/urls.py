from django.urls import path, include
from rest_framework import routers
from .views import EnterpriseView

router = routers.DefaultRouter()
router.register(r'enterprises', EnterpriseView, 'enterprises')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]