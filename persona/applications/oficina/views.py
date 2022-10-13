from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from .models import Oficina
from applications.empleado.models import Empleado

class oficinaListView(ListView):
    model = Oficina
    template_name = "oficina/lista.html"
    context_object_name = 'oficinas'

class oficinaDetailView(DetailView):
    model = Oficina
    template_name = "oficina/detalle.html"
    context_object_name = 'detalle'
    
    def get_context_data(self, **kwargs):
        context = super(oficinaDetailView, self).get_context_data(**kwargs)                 
        context['cant_empleados'] = Empleado.objects.filter(
            area__id = self.kwargs['pk']
        ).count()        
        return context