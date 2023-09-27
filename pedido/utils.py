import string
import random

from pedido.models import Pedido

def id_generator(size = 6, chars = string.ascii_uppercase + string.digits):
    the_id = "".join(random.choice(chars) for x in range(size))
    try:
        pedido = Pedido.objects.get(pedido_id = the_id)
        id_generator()
    except Pedido.DoesNotExist:
        return the_id