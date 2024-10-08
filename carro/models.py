from django.db import models
from django.urls import reverse

from producto.models import Producto, Variacion


class Carro(models.Model):
    #items = models.ManyToManyField(CartItem, blank=True)
    #productos = models.ManyToManyField(Producto, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Carro id: {self.id}"
    

class CarroItemManager(models.Manager):
    def orderByTimestamp(self):
        return super(CarroItemManager, self).order_by("timestamp")

class CarroItem(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    variaciones = models.ManyToManyField(Variacion, blank=True)
    cantidad = models.IntegerField(default=1)
    linea_total = models.DecimalField(default=10.99, max_digits=100,decimal_places=2)
    #notas = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CarroItemManager()

    def __str__(self):
        return self.producto.titulo     
    
    def get_borrar_item_url(self):
        return reverse("carro:borrar_item_carro", kwargs={"item_carroid":self.id})
