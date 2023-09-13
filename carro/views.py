from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from producto.models import Producto
from carro.models import Carro

def vista(request):
    msj_articulos = ""
    carro_vacio = False

    the_id = request.session.get('carro_id')
    print(the_id)
    if the_id:
        carro = Carro.objects.get(id=the_id)
        
        if carro.productos.all().count() == 0:
            carro_vacio = True
        elif carro.productos.all().count() == 1:
            msj_articulos = f"{carro.productos.all().count()} artículo"
        elif carro.productos.all().count() > 1:
            msj_articulos = f"{carro.productos.all().count()} artículos"

        context = {
            "carro": carro,
            "carro_vacio":carro_vacio,
            "msj_articulos":msj_articulos
        }
    elif the_id == None:
        context = {
            'carro_vacio': True
        }
    
    return render(request, "carros/vista.html", context)


def update_to_cart(request, slug):
    request.session.set_expiry(12000)
    nuevo_total = 0.00
    url = request.GET['url']
    
    the_id = request.session.get('carro_id')
    print(the_id)
    if the_id == None:
        nuevo_carro = Carro()
        nuevo_carro.save()
        request.session['carro_id'] = nuevo_carro.id
        the_id = nuevo_carro.id
    
    carro = Carro.objects.get(id=the_id)
    producto = get_object_or_404(Producto, slug=slug)

    if not producto in carro.productos.all():
        carro.productos.add(producto)
    else:
        carro.productos.remove(producto)
    
    for item in carro.productos.all():
        nuevo_total += float(item.precio)
    
    request.session['items_total'] = carro.productos.count()
    carro.total = nuevo_total
    carro.save()
    
    #return redirect("carro:vista")
    #return redirect('producto:all')
    return redirect(url)
    

def borrar_carro(request):
    the_id = request.session['carro_id']
    carro = Carro.objects.get(id=the_id)
    """
    for producto in carro.productos.all():
        carro.productos.remove(producto)
    """
    carro.productos.clear()
    carro.total = 0
    carro.save()
    request.session["items_total"] = 0
    return redirect("carro:vista")
