from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categoria_list = Categoria.objects.order_by('nombre')[:3]
    context = {
        'product_list': product_list,
        'categoria_list': categoria_list
    }
    return render(request,'index.html', context)

def producto (request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categoria_list = Categoria.objects.order_by('nombre')[:3]
    context = {
        'producto': producto,
        'categoria_list': categoria_list
    }
    return render(request,'producto.html', context)

def categoria (request, categoria_id):
    categoria_list = Categoria.objects.order_by('nombre')[:3]
    categoriaName = Categoria.objects.get(pk=categoria_id)
    productos = Producto.objects.filter(categoria = categoria_id)
    
    context = {
        'productos': productos,
        'categoria_list': categoria_list,
        'categoriaName': categoriaName
    }
    
    return render(request, 'categoria.html', context)