from rest_framework import viewsets
from .serializer import ProviderSerializer
from .models import Provider, ProviderType

class ProviderView(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class ProviderTypeView(viewsets.ModelViewSet):
    queryset = ProviderType.objects.all()
    serializer_class = ProviderSerializer


# Create your views here.
