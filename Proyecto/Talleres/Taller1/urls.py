from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
# Ruta para mostrar el formulario inicial
path('formulario/', views.mostrar_formulario, name='formulario_inicial'),
path('destino/', views.pagina_destino, name='devuelve_datos'),
]