import time
from django.shortcuts import render, redirect

from carro.models import Carro
from pedido.models import Pedido

def pedido(request):

    the_id = request.session.get("carro_id")
    if the_id == None:
        return redirect("carro:vista")
    print(the_id)
    carro = Carro.objects.get(id=the_id)

    nuevo_pedido, created = Pedido.objects.get_or_create(carro=carro)
    if created:
        #asignar un usuario a la orden

        nuevo_pedido.pedido_id = str(time.time())
        nuevo_pedido.save()

    if nuevo_pedido.estado == "Finished":
        carro.delete()
        del request.session['carro_id']
        del request.session['items_total']

        return redirect('carro:vista')
    
    return render(request, "pedidos/pedido.html")

