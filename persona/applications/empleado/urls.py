from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'empleado_app'

urlpatterns = [
    path(
        'inicial/',
        views.Inicio.as_view(),
        name='Pagina Inicial'
    ),
    path(
        'lista/',
        views.EmpleadoListView.as_view(),
        name='Lista de empleados'
    ),
    path(
        'buscar/',
        views.BuscarEmpleadoListView.as_view(),
        name='Buscar empleado'
    ),
    path(
        'detalle/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='Detalle del empleado'
    ),
    path(
        'create/',
        views.EmpleadoCreateView.as_view(),
        name='Alta de empleado'
    ),
    path(
        'update/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='Modificar empleado'
    ),
    path(
        'delete/<pk>/',
        views.EmpleadoDeleteView.as_view(),
        name='Baja de empleado'
    ),


]