from rest_framework import viewsets
from .serializer import EnterpriseSerializer
from .models import Enterprise

class EnterpriseView(viewsets.ModelViewSet):
    serializer_class = EnterpriseSerializer
    queryset = Enterprise.objects.all()
