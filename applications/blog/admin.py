from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(datosPersonales)
admin.site.register(datosPublicos)
admin.site.register(contenido_menu)




class catAdmin(admin.ModelAdmin):
    list_display = ('id','cod_categoria', 'nombre')  

admin.site.register(categorias,catAdmin)


class contAdmin(admin.ModelAdmin):
     list_display = [field.name for field in contenido._meta.get_fields()] 



admin.site.register(contenido,contAdmin)



