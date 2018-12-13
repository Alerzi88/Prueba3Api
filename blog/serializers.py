from .models import cliente
from .models import orden
from .models import tecnico
from rest_framework import serializers

class ClienteSerializer( serializers.HyperlinkedModelSerializer ):

    class Meta:
        model = cliente
        fields = ( 'telefono', 'ciudad', 'nombre', 'direccion', 'comuna', 'correo' )

class TecnicoSerializer( serializers.HyperlinkedModelSerializer ):

    class Meta:
        model = tecnico
        fields = ( 'NombreTecnico', 'ClienteAsignado' )

class OrdenSerializer( serializers.HyperlinkedModelSerializer ):

    class Meta:
        model = orden
        fields = ( 'clienteAtendido', 'Fecha', 'horaInicio', 'horaTermino', 'idAscensor', 'modeloAscensor', 'fallasDetectadas', 'reparacionesEfectuadas', 'piezasCambiadas', 'nombreTrabajador' )                