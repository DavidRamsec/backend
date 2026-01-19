from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from .forms import AutorForm
# 1. READ (Listar todos los autores)
def autor_list(request):
 """Muestra una lista de todos los autores."""
 autores = Autor.objects.all()
 contexto = {'autores': autores}
 return render(request, 'autor/autor_list.html', contexto)
# 2. CREATE (Crear un nuevo autor)
def autor_create(request):
 """Permite crear un nuevo autor."""
 if request.method == 'POST':
    form = AutorForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('autor_list')
 # Redirige a la lista después de guardar
 else:
 # Crea un formulario vacío para la petición GET
    form = AutorForm()

 contexto = {'form': form, 'titulo': 'Crear Nuevo Autor'}
 return render(request, 'autor/autor_form.html', contexto)
# 3. UPDATE (Editar un autor existente)
def autor_update(request, pk):
 """Permite editar un autor existente."""
 # Obtiene el autor o devuelve 404 si no existe
 autor = get_object_or_404(Autor, pk=pk)

 if request.method == 'POST':
 # Instancia el formulario con los datos POST y la instancia del autor
    form = AutorForm(request.POST, instance=autor)
    if form.is_valid():
        form.save()
        return redirect('autor_list')
 else:
 # Instancia el formulario con los datos del autor (para mostrar los datos actuales)
    form = AutorForm(instance=autor)
    contexto = {'form': form, 'titulo': f'Editar Autor: {autor}', 'autor':
    autor}
 return render(request, 'autor/autor_form.html', contexto)
# 4. DELETE (Eliminar un autor)
def autor_delete(request, pk):
 """Permite eliminar un autor."""
 autor = get_object_or_404(Autor, pk=pk)

 if request.method == 'POST':
    autor.delete()
    return redirect('autor_list')

 contexto = {'autor': autor}
 # Usaremos una plantilla de confirmación de borrado
 return render(request, 'autor/autor_confirm_delete.html', contexto)