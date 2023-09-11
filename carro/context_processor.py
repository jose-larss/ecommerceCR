from carro.models import Carro

def vista_previa_cesta(request):
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
            "previo_carro": carro,
            "previo_carro_vacio":carro_vacio,
            "previo_msj_articulos":msj_articulos
        }
    elif the_id == None:
        context = {
            'previo_carro_vacio': True
        }

    return context