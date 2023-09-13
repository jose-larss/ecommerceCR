from carro.models import Carro

def vista_previa_cesta(request):
    carro_vacio = False

    the_id = request.session.get('carro_id')
    if the_id:
        carro = Carro.objects.get(id=the_id)
        
        if carro.productos.all().count() == 0:
            carro_vacio = True

        context = {
            "previo_carro": carro,
            "previo_carro_vacio":carro_vacio,
        }
    elif the_id == None:
        context = {
            'previo_carro_vacio': True
        }
  
    return context