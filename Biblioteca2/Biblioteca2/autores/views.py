# autores/views.py
from django.views.generic import (
 CreateView, ListView, DetailView, UpdateView, DeleteView
)
from .models import Autor
from django.urls import reverse_lazy
# Vistas de Autor
class AutorListView(ListView): # R (Read/Listar)
 model = Autor
 template_name = 'autores/autor_list.html'

class AutorDetailView(DetailView): # R (Read/Detalle)
 model = Autor
 template_name = 'autores/autor_detail.html'
class AutorCreateView(CreateView): # C (Create/Crear)
 model = Autor
 fields = '__all__' # Incluye todos los campos del modelo
 template_name = 'autores/autor_form.html'
 success_url = reverse_lazy('autor-list') # A dónde ir después de crear
class AutorUpdateView(UpdateView): # U (Update/Actualizar)
 model = Autor
 fields = '__all__'
 template_name = 'autores/autor_form.html'
 success_url = reverse_lazy('autor-list')
class AutorDeleteView(DeleteView): # D (Delete/Eliminar)
 model = Autor
 template_name = 'autores/autor_confirm_delete.html'
 success_url = reverse_lazy('autor-list')
