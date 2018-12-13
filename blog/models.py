from django.db import models
from django import forms
from django.utils import timezone

class cliente(models.Model):

    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=25)
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)

class tecnico(models.Model):

    NombreTecnico = models.CharField(max_length=45)
    ClienteAsignado = models.CharField(max_length=45)

    def clienteasignado(self):
        self.save()

    def __str__(self):
        cadena = "Al Tecnico {0} Se le asigno el cliente {1}"
        return cadena.format(self.NombreTecnico, self.ClienteAsignado)  

class orden(models.Model):

    clienteAtendido = models.CharField(max_length=45)
    Fecha = models.DateTimeField(blank=True, null=True)
    horaInicio = models.DateTimeField(blank=True, null=True)
    horaTermino = models.DateTimeField(blank=True, null=True)
    idAscensor = models.IntegerField()
    modeloAscensor = models.CharField(max_length=40)
    fallasDetectadas = models.TextField()
    reparacionesEfectuadas = models.TextField()
    piezasCambiadas = models.CharField(max_length=200)
    nombreTrabajador = models.CharField(max_length=45)

    def fechaAtencion(self):
        self.Fecha = timezone.now()
        self.save()
    def fechaInicio(self):
        self.horaInicio = timezone.now()
        self.save()
    def fechaTermino(self):
        self.horaTermino = timezone.now()
        self.save()        

 

