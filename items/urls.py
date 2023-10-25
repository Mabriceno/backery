from django.urls import path, include
from rest_framework import routers
from .views import ItemView, ItemCategoryView

router = routers.DefaultRouter()
router.register(r'items', ItemView, 'items')
router.register(r'items-categories', ItemCategoryView, 'items-categories')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
