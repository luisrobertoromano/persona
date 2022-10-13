from django.contrib import admin
from .models import Empleado, Habilidad

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'apellidos',
        'nombres',
        'nombre_completo',
        'dni',        
        'area',
    )

    search_fields = ('apellidos',)
    list_filter = ('area','habilidades',)
    #filter_horizontal = ('habilidades',)


admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidad)