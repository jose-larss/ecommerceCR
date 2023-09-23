from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from producto.models import Producto, Variacion
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


def add_to_cart(request, slug):
    request.session.set_expiry(12000)
    nuevo_total = 0.00
    #notas = {} 
    product_var = []

    url = request.GET.get('url')

    the_id = request.session.get('carro_id')
    print(the_id)
    if the_id == None:
        nuevo_carro = Carro()
        nuevo_carro.save()
        request.session['carro_id'] = nuevo_carro.id
        the_id = nuevo_carro.id
    
    carro = Carro.objects.get(id=the_id)
    producto = get_object_or_404(Producto, slug=slug)

    if request.method == "POST":
        qty = request.POST["qty"]
        #color = request.POST["color"]
        #size = request.POST["size"]
        for item in request.POST:
            key = item
            val = request.POST[key]
            print(key, val)
            try:
                v = Variacion.objects.get(producto=producto, variacion__iexact=key, titulo__iexact = val)
                product_var.append(v)
            except:
                pass
        print(product_var)

        #cart_item, created = CarroItem.objects.get_or_create(carro=carro, producto=producto)
        #if created:
        #    print("creado")
        cart_item = CarroItem.objects.create(carro=carro, producto=producto)

        #if int(qty) <= 0:
        #    cart_item.delete()
        #else:
        if len(product_var) > 0:
            #antes de grabar las nuevas variaciones, hay que borrar las que hubiera
            #cart_item.variaciones.clear()
            #for item in product_var:
            cart_item.variaciones.add(*product_var)
        
        cart_item.cantidad = qty
        #cart_item.notas = notas
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
    else:
        return redirect(url)


def borrar_item_carro(request, item_carroid):
    nuevo_total = 0.00

    url = request.GET.get("url")
    the_id = request.session.get('carro_id') 

    #cojo carro_item en base a id que viene por parametro y lo pongo a None
    cart_item = CarroItem.objects.get(id=item_carroid)
    cart_item.carro = None
    cart_item.save()

    #Cojo carro contabilizo su total
    carro = Carro.objects.get(id=the_id)
    for item in carro.carroitem_set.all(): 
        linea_total = float(item.producto.precio) * item.cantidad
        nuevo_total += linea_total

    #Actualizo total items en en session y grabo total de carro
    request.session['items_total'] = carro.carroitem_set.count()
    carro.total = nuevo_total
    carro.save()

    if url:
        return redirect(url)
    return redirect("carro:vista")
  
    
    
def borrar_carro(request):
    the_id = request.session.get('carro_id')
    carro = Carro.objects.get(id=the_id)
    """
    for producto in carro.productos.all():
        carro.productos.remove(producto)
    """
    carro.carroitem_set.clear()
    carro.total = 0
    carro.save()
    request.session["items_total"] = 0
    return redirect("carro:vista")
