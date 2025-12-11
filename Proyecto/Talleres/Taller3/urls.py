from django.urls import path
from .views import ( LibroListView, LibroDetailView, LibroCreateView,
                     LibroUpdateView, LibroDeleteView)

urlpatterns = [
    # READ (Lista)
    path('', LibroListView.as_view(), name='libro_list'),

    # READ (Detalle) - Necesita la clave primaria (pk)
    path('<int:pk>/', LibroDetailView.as_view(), name='libro_detail'),

    # CREATE
    path('nuevo/', LibroCreateView.as_view(), name='libro_create'),

    # UPDATE - Necesita la clave primaria (pk)
    path('<int:pk>/editar/', LibroUpdateView.as_view(),
         name='libro_update'),

    # DELETE - Necesita la clave primaria (pk)
    path('<int:pk>/eliminar/', LibroDeleteView.as_view(),
         name='libro_delete'),
]