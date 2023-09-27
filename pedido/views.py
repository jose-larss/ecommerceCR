from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

#from pedido.utils import id_generator

from carro.models import Carro
from pedido.models import Pedido


#@method_decorator(login_required, name="dispatch")
@login_required
def checkout(request):

    the_id = request.session.get("carro_id")
    if the_id == None:
        return redirect("carro:vista")
    print(the_id)
    carro = Carro.objects.get(id=the_id)

    nuevo_pedido, created = Pedido.objects.get_or_create(carro=carro)
    if created:
        nuevo_pedido.carro = carro
        nuevo_pedido.usuario = request.user
        nuevo_pedido.save()       
    """
    try:
        nuevo_pedido= Pedido.objects.get(carro=carro)
    except Pedido.DoesNotExist:
        nuevo_pedido = Pedido()
        nuevo_pedido.carro = carro
        nuevo_pedido.usuario = request.user
        nuevo_pedido.save()
    """
    if nuevo_pedido.estado == "Finished":
        carro.delete()
        del request.session['carro_id']
        del request.session['items_total']

        return redirect('carro:vista')
    
    return render(request, "pedidos/pedido.html")


def pedidos(request):
    return render(request, "pedidos/user.html")



