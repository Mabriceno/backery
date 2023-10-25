from rest_framework import viewsets
from .serializer import ItemSerializer, ItemCategorySerializer
from .models import Item, ItemCategory

class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ItemCategoryView(viewsets.ModelViewSet):
    serializer_class = ItemCategorySerializer
    queryset = ItemCategory.objects.all()
