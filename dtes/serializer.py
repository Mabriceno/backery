from rest_framework import serializers
from .models import DteType

class DteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DteType
        fields = '__all__'

