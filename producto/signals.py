from .models import Variacion

def product_default(sender, instance, created, *args, **kwargs):
    
    if instance.update_defaults:
        print(instance.update_defaults)
        #if created:
        categorias = instance.categoria.all()
        print(categorias)
        for cat in categorias:
            if cat.id == 1: # Categoria ropa
                print(cat.id)
                extra_small_size = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "XS")
                small_size = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "S")
                medium_size = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "M")
                large_size = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "L")
                extra_Large_size = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "XL")
                extra_Double_size = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "XXL")
                extra_Triple_size = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "3XL")
            if cat.id == 2:
                print(cat.id)
                size_37 = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "37")
                size_38 = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "38")
                size_39 = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "39")
                size_40 = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "40")  
                size_41 = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "41")
                size_42 = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "42")
                size_43 = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "43")
                size_44 = Variacion.objects.get_or_create(producto = instance,
                                                                variacion = "size",
                                                                titulo = "44")                
        #esto es importante ya que sino se convertoria en un bucle infinito
        instance.update_defaults = False
        instance.save()