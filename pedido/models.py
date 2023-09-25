from django.db import models

from carro.models import Carro

STATUS_CHOICES = (
    ('Started', 'started'),
    ('Abandoned', 'abandoned'),
    ('Finished', 'finished'),
)

class Pedido(models.Model):
    # add user
    # add adress
    pedido_id = models.CharField(max_length=120, unique=True)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    estado = models.CharField(max_length=120, choices=STATUS_CHOICES, default='started')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pedido_id
