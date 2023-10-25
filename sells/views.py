from rest_framework import viewsets
from .serializer import SellSerializer, ItemSellSerializer, DocumentSellReferenceSerializer
from .models import Sell, ItemSell, DocumentSellReference

class SellView(viewsets.ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

class ItemSellView(viewsets.ModelViewSet):
    queryset = ItemSell.objects.all()
    serializer_class = ItemSellSerializer

class DocumentSellReferenceView(viewsets.ModelViewSet):
    queryset = DocumentSellReference.objects.all()
    serializer_class = DocumentSellReferenceSerializer


