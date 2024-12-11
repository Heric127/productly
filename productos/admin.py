from django.contrib import admin
from .models import categoria, producto
# Register your models here.


class categoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class productoAdmin(admin.ModelAdmin):
    exclude = ('creado_en', )
    list_display = ('id', 'nombre', 'stock', 'creado_en')


admin.site.register(categoria, categoriaAdmin)
admin.site.register(producto, productoAdmin)
