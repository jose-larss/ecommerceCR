import uuid
from django.conf import settings
from django.db import models

from carro.models import Carro

User = settings.AUTH_USER_MODEL

STATUS_CHOICES = (
    ('Started', 'started'),
    ('Abandoned', 'abandoned'),
    ('Finished', 'finished'),
)

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    pedido_id = models.UUIDField(default=uuid.uuid4, editable=False)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    estado = models.CharField(max_length=120, choices=STATUS_CHOICES, default='started')
    # add adress
    sub_total = models.DecimalField(default=10.99, max_digits=100, decimal_places=2)
    tax_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    final_total = models.DecimalField(default=10.99, max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.pedido_id
