# libro/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
# --- READ (Listar y Detalle) ---
def lista_libros(request):
 """
 Lista todos los libros (READ - Lista).
 """
 libros = Libro.objects.all()
 return render(request, 'libro/lista.html', {'libros': libros})
def detalle_libro(request, libro_id):
 """
 Muestra los detalles de un libro específico (READ - Detalle).
 """
 libro = get_object_or_404(Libro, pk=libro_id)
 return render(request, 'libro/detalle.html', {'libro': libro})
# --- CREATE (Crear) ---
def crear_libro(request):
 """
 Permite crear un nuevo libro (CREATE).
 Maneja la lógica de validación e inserción manual.
 """
 if request.method == 'POST':
   # Accedemos a los datos directamente del diccionario request.POST
    titulo = request.POST.get('titulo')
    autor = request.POST.get('autor')
    fecha_publicacion = request.POST.get('fecha_publicacion')
    # Simple validación (debería ser más robusta en producción)
    if titulo and autor:
      Libro.objects.create(
      titulo=titulo,
      autor=autor,
      fecha_publicacion=fecha_publicacion if fecha_publicacion
         else None
      )
      return redirect('lista_libros') # Redirigir a la lista después de crear
 return render(request, 'libro/crear.html')
# --- UPDATE (Actualizar) ---
def editar_libro(request, libro_id):
 """
 Permite editar un libro existente (UPDATE).
 """
 libro = get_object_or_404(Libro, pk=libro_id)
 if request.method == 'POST':
    libro.titulo = request.POST.get('titulo')
    libro.autor = request.POST.get('autor')
    fecha_publicacion = request.POST.get('fecha_publicacion')

    # Guardamos el objeto actualizado
    if libro.titulo and libro.autor:
      libro.fecha_publicacion = fecha_publicacion if fecha_publicacion else None
      libro.save()
      return redirect('detalle_libro', libro_id=libro.id)
 return render(request, 'libro/editar.html', {'libro': libro})
# --- DELETE (Borrar) ---
def borrar_libro(request, libro_id):
 """
 Elimina un libro (DELETE).
 """
 libro = get_object_or_404(Libro, pk=libro_id)

 if request.method == 'POST':
    libro.delete()
    return redirect('lista_libros')

 # Usaremos el mismo template para confirmar la eliminación
 return render(request, 'libro/confirmar_borrar.html', {'libro': libro})

def tratar_libro(request, libro_id=None):
   print(libro_id)
   if(libro_id):
      libro = get_object_or_404(Libro, pk=libro_id)
      if request.method == 'POST':
         libro.titulo = request.POST.get('titulo')
         libro.autor = request.POST.get('autor')
         fecha_publicacion = request.POST.get('fecha_publicacion')

         # Guardamos el objeto actualizado
         if libro.titulo and libro.autor:
            libro.fecha_publicacion = fecha_publicacion if fecha_publicacion else None
            libro.save()
            return redirect('detalle_libro', libro_id=libro.id)
      return render(request, 'libro/mi_editar.html', {'libro': libro})
   else:
      if request.method == 'POST':
         # Accedemos a los datos directamente del diccionario request.POST
         titulo = request.POST.get('titulo')
         autor = request.POST.get('autor')
         fecha_publicacion = request.POST.get('fecha_publicacion')
         # Simple validación (debería ser más robusta en producción)
         if titulo and autor:
            Libro.objects.create(
            titulo=titulo,
            autor=autor,
            fecha_publicacion=fecha_publicacion if fecha_publicacion
               else None
            )
            return redirect('lista_libros') # Redirigir a la lista después de crear
      return render(request, 'libro/mi_editar.html')