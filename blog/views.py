from .models import perro
from rest_framework import viewsets
from blog.serializers import DogSerializer


class DogViewSet( viewsets.ModelViewSet ):
    queryset = perro.objects.all()
    serializer_class = DogSerializer
    
    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj
