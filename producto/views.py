from django.shortcuts import render

from producto.models import Producto


def all_products(request):
    productos = Producto.objects.all()
    context = {
        "productos": productos,
    }
    return render(request, "productos/all_productos.html", context)