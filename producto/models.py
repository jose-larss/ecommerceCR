from django.db.models.query import QuerySet
from django.urls import reverse

from django.db import models

class CategoriaManager(models.Manager):
    def categoriasActivas(self):
        return super(CategoriaManager, self).filter(active=True)

class Categoria(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    presentada = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = CategoriaManager()

    class Meta:
        unique_together = ["titulo", "slug"]
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo

class ProductoQueryset(models.QuerySet):
    def productosActivosxcategoria(self, slug=None):
        if slug is None:
            return self.filter(active=True, categoria=5)
        categoria = Categoria.objects.get(slug=slug)
        return self.filter(active=True, categoria=categoria)    

class ProductoManager(models.Manager):
    def get_queryset(self):
        return ProductoQueryset(self.model, using=self._db)

    def filtrar(self, slug = None):
        return self.get_queryset().productosActivosxcategoria(slug=slug)


class Producto(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(null=True, blank=True)
    categoria = models.ManyToManyField(Categoria, blank=True)
    precio = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    #Este campo me da que nunca lo uso
    #precio_venta = models.DecimalField(decimal_places=2, max_digits=100,\
    #                                                        null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = ProductoManager()

    class Meta:
        unique_together = ['titulo', 'slug']
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("producto:single_producto", kwargs={'slug':self.slug})
    

class ProductoImagenManager(models.Manager):
    def fotoActivaNoPresentada(self):
        return super(ProductoImagenManager, self).filter(active=True, presentada=False)

    def fotoActivaPresentada(self):
        return super(ProductoImagenManager, self).filter(active=True, presentada=True)

class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos/imagenes")
    presentada = models.BooleanField(default=False)
    miniatura = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ProductoImagenManager()

    class Meta:
        verbose_name = "Producto Imagen"
        verbose_name_plural = "Productos Imagenes"

    def __str__(self):
        return self.producto.titulo



