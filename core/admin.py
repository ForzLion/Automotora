from django.contrib import admin
from .models import Marca, Automovil
# Register your models here.

#configuraremos la entidad automovil
#en el admin de django
class AutomovilAdmin(admin.ModelAdmin):
    #en las tuplas los elementos
    #no son modificables
    list_display = ('patente', 'anio', 'modelo')
    #agregaremos una caja de busqueda
    search_fields = ['patente', 'modelo']

admin.site.register(Marca)
admin.site.register(Automovil, AutomovilAdmin)