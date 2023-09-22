from django.apps import AppConfig
from django.db.models.signals import post_save

class ProductoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'producto'

    def ready(self):
        from producto.signals import product_default
        from producto.models import Producto

        post_save.connect(product_default, sender=Producto)
        
