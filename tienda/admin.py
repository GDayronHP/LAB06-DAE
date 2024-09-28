from django.contrib import admin

from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pub_date')  
    list_filter = ('nombre',)  
    search_fields = ('nombre', 'pub_date') 
    ordering = ('nombre',) 

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre', 'precio', 'stock', 'pub_date')  
    list_filter = ('categoria',)  
    search_fields = ('categoria', 'nombre')  
    ordering = ('categoria',)  
