# Libros/models.py

from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    # Relación uno a muchos: un Autor puede tener muchos Libros
    fecha_publicacion = models.DateField(null=True, blank=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    autor = models.ForeignKey('autores.Autor', on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo