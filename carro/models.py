from django.db import models

from producto.models import Producto

class Carro(models.Model):
    productos = models.ManyToManyField(Producto, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Carro id: {self.id}"
    
