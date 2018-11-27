from .models import perro
from rest_framework import serializers

class DogSerializer( serializers.HyperlinkedModelSerializer ):
   
    class Meta:
        model = perro
        fields = ( 'edad', 'raza', 'nombre', 'estado', 'descripcion' )