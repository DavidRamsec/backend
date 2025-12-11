from django.db import models

# Create your models here.
class Autor(models.Model):
 nombre = models.CharField(max_length=100)
 apellido = models.CharField(max_length=100)
 fecha_nacimiento = models.DateField(null=True, blank=True)
 def __str__(self):
    return f'{self.apellido}, {self.nombre}'

class Libro(models.Model):
 titulo = models.CharField(max_length=200)
 # Relación uno a muchos: un Autor puede tener muchos Libros
 autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
 fecha_publicacion = models.DateField(null=True, blank=True)
 isbn = models.CharField('ISBN', max_length=13, unique=True)

 def __str__(self):
    return self.titulo
