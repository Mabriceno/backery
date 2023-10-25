from rest_framework import serializers
from .models import Sell, ItemSell, DocumentSellReference

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'

class ItemSellSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSell
        fields = '__all__'

class DocumentSellReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentSellReference
        fields = '__all__'
