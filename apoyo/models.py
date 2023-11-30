from django.db import models
from django.contrib.auth.models import User

# Create your models here. 
class Donacion(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Celular = models.IntegerField(default=569)
    Direccion = models.CharField(max_length=100)
    Comuna = models.CharField(max_length=100)
    Fecha = models.DateTimeField(auto_now_add=True)
    Monto = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Donacion de ' + self.Nombre 
    
Genero_select = [
    (1, 'Masculino'),
    (2, 'Femenino')
]

class AddPatient(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Run = models.CharField(max_length=10)
    Genero = models.IntegerField(null=False, blank=False, choices= Genero_select)
    Direccion = models.CharField(max_length=100)
    Comuna = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'Paciente ' + self.Nombre