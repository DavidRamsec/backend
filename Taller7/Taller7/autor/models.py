# autores/models.py
from django.db import models
class Autor(models.Model):
 nombre = models.CharField(max_length=100)
 apellido = models.CharField(max_length=100)
 fecha_nacimiento = models.DateField(null=True, blank=True)
 def __str__(self):
    return f'{self.apellido}, {self.nombre}'