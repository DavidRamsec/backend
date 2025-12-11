# libros/models.py  

from django.db import models  
from django.urls import reverse  

class Libro(models.Model):  
    titulo = models.CharField(max_length=200)  
    autor = models.CharField(max_length=100)  
    fecha_publicacion = models.DateField()  
    
    def __str__(self):  
        return self.titulo  
    
    # Define dónde ir después de crear/actualizar un libro  
    def get_absolute_url(self):  
        return reverse('libro_detail', kwargs={'pk': self.pk})