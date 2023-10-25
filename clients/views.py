from rest_framework import viewsets
from .serializer import ClientSerializer, ClientTypeSerializer
from .models import Client, ClientType

class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class ClientTypeView(viewsets.ModelViewSet):
    serializer_class = ClientTypeSerializer
    queryset = ClientType.objects.all()
