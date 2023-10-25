from django.urls import path, include
from rest_framework import routers
from .views import SellView, ItemSellView, DocumentSellReferenceView

router = routers.DefaultRouter()
router.register(r'sells', SellView, 'sells')
router.register(r'items_sells', ItemSellView, 'items_sell')
router.register(r'document_sell_reference', DocumentSellReferenceView, 'document_sell_reference')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]