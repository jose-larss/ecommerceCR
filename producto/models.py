from django.db import models

class Producto(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    #Este campo me da que nunca lo uso
    #precio_venta = models.DecimalField(decimal_places=2, max_digits=100,\
    #                                                        null=True, blank=True)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
    def get_precio(self):
        return self.precio
    

class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos/imagenes")
    presentada = models.BooleanField(default=False)
    miniatura = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto Imagen"
        verbose_name_plural = "Productos Imagenes"

    def __str__(self):
        return self.producto.titulo



