from django.shortcuts import render

# Create your views here.
# libros/views.py
from django.views.generic import (
 CreateView, ListView, DetailView, UpdateView, DeleteView
)
from .models import Autor, Libro
from django.urls import reverse_lazy
# Vistas de Autor
class AutorListView(ListView): # R (Read/Listar)
 model = Autor
 template_name = 'libros/autor_list.html'

class AutorDetailView(DetailView): # R (Read/Detalle)
 model = Autor
 template_name = 'libros/autor_detail.html'
class AutorCreateView(CreateView): # C (Create/Crear)
 model = Autor
 fields = '__all__' # Incluye todos los campos del modelo
 template_name = 'libros/autor_form.html'
 success_url = reverse_lazy('autor-list') # A dónde ir después de crear
class AutorUpdateView(UpdateView): # U (Update/Actualizar)
 model = Autor
 fields = '__all__'
 template_name = 'libros/autor_form.html'
 success_url = reverse_lazy('autor-list')
class AutorDeleteView(DeleteView): # D (Delete/Eliminar)
 model = Autor
 template_name = 'libros/autor_confirm_delete.html'
 success_url = reverse_lazy('autor-list')

# --------------------------
# Vistas de Libro (CRUD)
# --------------------------
class LibroListView(ListView): # R: Listar todos los libros
 model = Libro
 template_name = 'libros/libro_list.html'

class LibroDetailView(DetailView): # R: Mostrar el detalle de un libro
 model = Libro
 template_name = 'libros/libro_detail.html'
class LibroCreateView(CreateView): # C: Crear un nuevo libro
 model = Libro
 # Campos a incluir en el formulario (ForeignKey a Autor se renderiza como un selector)
 fields = ['titulo', 'autor', 'fecha_publicacion', 'isbn']
 template_name = 'libros/libro_form.html'
 success_url = reverse_lazy('libro-list') # Redirige a la lista después de crear
class LibroUpdateView(UpdateView): # U: Actualizar un libro existente
 model = Libro
 fields = ['titulo', 'autor', 'fecha_publicacion', 'isbn']
 template_name = 'libros/libro_form.html'
 success_url = reverse_lazy('libro-list')
class LibroDeleteView(DeleteView): # D: Eliminar un libro
 model = Libro
 template_name = 'libros/libro_confirm_delete.html'
 success_url = reverse_lazy('libro-list')