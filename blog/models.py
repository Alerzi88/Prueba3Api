from django.db import models

class perro(models.Model):

    rescatado = 'Rescatado'
    disponible = 'Disponible'
    adoptado = 'Adoptado'

    estados = (
        (rescatado, 'Rescatado'),
        (disponible, 'Disponible'),
        (adoptado, 'Adoptado'),
    )
    
    edad = models.IntegerField()
    raza = models.CharField(max_length=25)
    nombre = models.CharField(max_length=30)
    estado = models.CharField(max_length=10, choices=estados, default=rescatado)
    descripcion = models.TextField( default="" )
   
