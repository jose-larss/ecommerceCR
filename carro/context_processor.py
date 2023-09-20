from carro.models import Carro

def vista_previa_cesta(request):
    carro_vacio = False

    the_id = request.session.get('carro_id')
    if the_id:
        carro = Carro.objects.get(id=the_id)
        
        if carro.carroitem_set.count() == 0:
            carro_vacio = True
        carro_items = carro.carroitem_set.orderByTimestamp
        context = {
            "previo_total":carro.total,
            "previo_carro": carro_items,
            "previo_carro_vacio":carro_vacio,
        }
    elif the_id == None:
        context = {
            'previo_carro_vacio': True
        }
  
    return context