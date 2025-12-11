from django.urls import path
from . import views
urlpatterns = [

 # Aquí mapearías las URLs para Libro
 # --------------------------
 # URLs para el Libro
 # --------------------------
 path('', views.LibroListView.as_view(), name='libro-list'),
 path('nuevo/', views.LibroCreateView.as_view(), name='libro-create'),
 # <int:pk> se usa para identificar el libro específico
 path('<int:pk>/', views.LibroDetailView.as_view(), name='librodetail'),
 path('<int:pk>/editar/', views.LibroUpdateView.as_view(), name='libroupdate'),
 path('<int:pk>/eliminar/', views.LibroDeleteView.as_view(),
name='libro-delete'),
]