from . import views
from django.urls import path

urlpatterns = [
    path(
        'lista-oficinas/',
        views.oficinaListView.as_view(),
        name='Lista de oficinas'
    ),
    path(
        'detalle-oficina/<pk>/',
        views.oficinaDetailView.as_view(),
        name='Detalle de la oficina'
    ),
]