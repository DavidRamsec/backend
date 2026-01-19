from django.urls import path
from . import views
urlpatterns = [
 # READ
 path('', views.autor_list, name='autor_list'),

 # CREATE
 path('nuevo/', views.autor_create, name='autor_create'),

 # UPDATE (usamos <int:pk> para identificar al autor)
 path('<int:pk>/editar/', views.autor_update, name='autor_update'),

 # DELETE
 path('<int:pk>/eliminar/', views.autor_delete, name='autor_delete'),
]
