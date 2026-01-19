# libro/urls.py
from django.urls import path
from . import views
urlpatterns = [
 # READ
 path('Libros/', views.lista_libros, name='lista_libros'),
 path('Libros/<int:libro_id>/', views.detalle_libro,
name='detalle_libro'),

 # CREATE
 path('Libros/nuevo/', views.crear_libro, name='crear_libro'),

 # UPDATE
 path('Libros/<int:libro_id>/editar/', views.editar_libro,
name='editar_libro'),

 # DELETE
 path('Libros/<int:libro_id>/borrar/', views.borrar_libro,
name='borrar_libro'),
 
 # CREATE
 path('Libros/tratar/', views.tratar_libro,
name='tratar_libro'),
 
 # UPDATE
 path('Libros/tratar/<int:libro_id>/', views.tratar_libro,
name='tratar_libro'),
]
