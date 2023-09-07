from django.shortcuts import render, redirect, get_object_or_404

from producto.models import Producto
from carro.models import Carro

def vista(request):
    msj_articulos = ""
    carro = Carro.objects.all()[0]

    if carro.productos.all().count() == 1:
        msj_articulos = f"{carro.productos.all().count()} artículo"
    elif carro.productos.all().count() > 1:
        msj_articulos = f"{carro.productos.all().count()} artículos"
    context = {
        "carro": carro,
        "msj_articulos":msj_articulos
    }
    return render(request, "carros/vista.html", context)

def update_to_cart(request, slug):
    carro = Carro.objects.all()[0]
    producto = get_object_or_404(Producto, slug=slug)

    if not producto in carro.productos.all():
        carro.productos.add(producto)
    else:
        carro.productos.remove(producto)
    
    nuevo_total = 0.00
    for item in carro.productos.all():
        nuevo_total += float(item.precio)
    
    print(nuevo_total)
    carro.total = nuevo_total
    carro.save()
    
    return redirect("carro:vista")
