from django.urls import path
from . import views
urlpatterns = [
 # URLs para el Autor
 path('', views.AutorListView.as_view(), name='autor-list'),
 path('nuevo/', views.AutorCreateView.as_view(), name='autor-create'),
 path('<int:pk>/', views.AutorDetailView.as_view(), name='autordetail'),
 path('<int:pk>/editar/', views.AutorUpdateView.as_view(), name='autorupdate'),
 path('<int:pk>/eliminar/', views.AutorDeleteView.as_view(),
name='autor-delete'),

]
