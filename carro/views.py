from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from producto.models import Producto
from carro.models import Carro, CarroItem

def vista(request):
    msj_articulos = ""
    carro_vacio = False

    the_id = request.session.get('carro_id')
    print(the_id)
    if the_id:
        carro = Carro.objects.get(id=the_id)
        
        if carro.carroitem_set.count() == 0:
            carro_vacio = True
        elif carro.carroitem_set.count() == 1:
            msj_articulos = f"{carro.carroitem_set.count()} artículo"
        elif carro.carroitem_set.all().count() > 1:
            msj_articulos = f"{carro.carroitem_set.count()} artículos"

        carro_items = carro.carroitem_set.orderByTimestamp

        context = {
            "carro": carro_items,
            "total":carro.total,
            "carro_vacio":carro_vacio,
            "msj_articulos":msj_articulos
        }
    elif the_id == None:
        context = {
            'carro_vacio': True
        }
    
    return render(request, "carros/vista.html", context)


def update_to_quantity(request):
    msj_articulos = ""
    nuevo_total = 0.00   

    slug = request.GET.get("slug")
    qty = request.GET.get("qty")
  
    the_id = request.session.get('carro_id')
    carro = Carro.objects.get(id=the_id)

    producto = get_object_or_404(Producto, slug=slug)
    cart_item = CarroItem.objects.get(carro=carro, producto=producto)

    cart_item.cantidad = qty
    cart_item.linea_total = float(cart_item.cantidad) * float(cart_item.producto.precio)
    cart_item.save()

    for item in carro.carroitem_set.all(): 
        linea_total = float(item.producto.precio) * item.cantidad
        nuevo_total += linea_total
    
    request.session['items_total'] = carro.carroitem_set.count()
    carro.total = nuevo_total
    carro.save()

    carro_items = carro.carroitem_set.orderByTimestamp

    if carro.carroitem_set.count() == 1:
        msj_articulos = f"{carro.carroitem_set.count()} artículo"
    elif carro.carroitem_set.all().count() > 1:
        msj_articulos = f"{carro.carroitem_set.count()} artículos"

    context = {
        "msj_articulos":msj_articulos,
        "carro":carro_items,
        "total": carro.total
    }
    return render(request, "componentes/vista_ajax_div.html", context)
    #return redirect("carro:vista")
    #return render(request, "carros/vista.html", context)

def update_to_cart(request, slug):
    request.session.set_expiry(12000)
    nuevo_total = 0.00
    url = request.GET.get('url')

    qty = request.GET.get("qty")
    color = request.GET.get("color")

    the_id = request.session.get('carro_id')
    print(the_id)
    if the_id == None:
        nuevo_carro = Carro()
        nuevo_carro.save()
        request.session['carro_id'] = nuevo_carro.id
        the_id = nuevo_carro.id
    
    carro = Carro.objects.get(id=the_id)
    producto = get_object_or_404(Producto, slug=slug)

    cart_item, created = CarroItem.objects.get_or_create(carro=carro, producto=producto)
    if created:
        print("creado")

    if int(qty) == 0:
        cart_item.delete()
    else:
        cart_item.cantidad = qty
        cart_item.linea_total = float(cart_item.cantidad) * float(cart_item.producto.precio)
        cart_item.save()
    """
    if not cart_item in carro.items.all():
        carro.items.add(cart_item)
    else:
        carro.items.remove(cart_item)
    """

    for item in carro.carroitem_set.all():
        linea_total = float(item.producto.precio) * item.cantidad
        nuevo_total += linea_total
    
    request.session['items_total'] = carro.carroitem_set.count()
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
