from rest_framework import viewsets
from .serializer import DteTypeSerializer
from .models import DteType

class DteTypeView(viewsets.ModelViewSet):
    serializer_class = DteTypeSerializer
    queryset = DteType.objects.all()
    
