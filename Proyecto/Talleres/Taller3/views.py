# libros/views.py
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Libro
from django.urls import reverse_lazy

# CRUD

# 1. READ (Lista)
class LibroListView(ListView):
    model = Libro
    template_name = 'Taller3/libro_list.html'
    # Nombre de la lista de objetos en la plantilla
    context_object_name = 'libro'

# 2. READ (Detalle)
class LibroDetailView(DetailView):
    model = Libro
    template_name = 'Taller3/libro_detail.html'

# 3. CREATE
class LibroCreateView(CreateView):
    model = Libro
    template_name = 'Taller3/libro_form.html'
    # Campos a mostrar en el formulario
    fields = ['titulo', 'autor', 'fecha_publicacion']

# 4. UPDATE
class LibroUpdateView(UpdateView):
    model = Libro
    template_name = 'Taller3/libro_form.html'
    fields = ['titulo', 'autor', 'fecha_publicacion']
    # Django automaticamente usará get_absolute_url()
    # del modelo para la redirección

# 5. DELETE
class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'Taller3/libro_confirm_delete.html'
    # A dónde ir después de la eliminación
    success_url = reverse_lazy('libro_list')