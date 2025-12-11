# autor/urls.py
from django.urls import path
from . import views
urlpatterns = [
 # READ
 path('', views.lista_autores, name='lista_autores'),
 path('<int:autor_id>/', views.detalle_autor,
name='detalle_autor'),

 # CREATE
 path('nuevo/', views.crear_autor, name='crear_autor'),

 # UPDATE
 path('<int:autor_id>/editar/', views.editar_autor,
name='editar_autor'),

 # DELETE
 path('<int:autor_id>/borrar/', views.borrar_autor,
name='borrar_autor'),
]
