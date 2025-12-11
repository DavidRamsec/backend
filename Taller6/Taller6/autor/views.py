# autor/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
# --- READ (Listar y Detalle) ---
def lista_autores(request):
 """
 Lista todos los autores (READ - Lista).
 """
 autores = Autor.objects.all()
 return render(request, 'autor/lista.html', {'autores': autores})
def detalle_autor(request, autor_id):
 """
 Muestra los detalles de un autor específico (READ - Detalle).
 """
 autor = get_object_or_404(Autor, pk=autor_id)
 return render(request, 'autor/detalle.html', {'autor': autor})
# --- CREATE (Crear) ---
def crear_autor(request):
 """
 Permite crear un nuevo autor (CREATE).
 Maneja la lógica de validación e inserción manual.
 """
 if request.method == 'POST':
   # Accedemos a los datos directamente del diccionario request.POST
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    # Simple validación (debería ser más robusta en producción)
    if nombre and apellido:
      Autor.objects.create(
      nombre=nombre,
      apellido=apellido,
      fecha_nacimiento=fecha_nacimiento if fecha_nacimiento
         else None
      )
      return redirect('lista_autores') # Redirigir a la lista después de crear
 return render(request, 'autor/crear.html')
# --- UPDATE (Actualizar) ---
def editar_autor(request, autor_id):
 """
 Permite editar un autor existente (UPDATE).
 """
 autor = get_object_or_404(Autor, pk=autor_id)
 if request.method == 'POST':
    autor.nombre = request.POST.get('nombre')
    autor.apellido = request.POST.get('apellido')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')

    # Guardamos el objeto actualizado
    if autor.nombre and autor.apellido:
      autor.fecha_nacimiento = fecha_nacimiento if fecha_nacimiento else None
      autor.save()
      return redirect('detalle_autor', autor_id=autor.id)
 return render(request, 'autor/editar.html', {'autor': autor})
# --- DELETE (Borrar) ---
def borrar_autor(request, autor_id):
 """
 Elimina un autor (DELETE).
 """
 autor = get_object_or_404(Autor, pk=autor_id)

 if request.method == 'POST':
    autor.delete()
    return redirect('lista_autores')

 # Usaremos el mismo template para confirmar la eliminación
 return render(request, 'autor/confirmar_borrar.html', {'autor': autor})