from .models import cliente
from .models import orden
from .models import tecnico
from rest_framework import viewsets
from blog.serializers import ClienteSerializer
from blog.serializers import OrdenSerializer
from blog.serializers import TecnicoSerializer


class ClienteViewSet( viewsets.ModelViewSet ):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer
    
    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

class TecnicoViewSet( viewsets.ModelViewSet ):
    queryset = tecnico.objects.all()
    serializer_class = TecnicoSerializer
    
    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

class OrdenViewSet( viewsets.ModelViewSet ):
    queryset = orden.objects.all()
    serializer_class = OrdenSerializer
    
    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj
