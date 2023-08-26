from django.contrib import admin

from producto.models import Producto, ProductoImagen

class ProductoAdmin(admin.ModelAdmin):
    date_hierarchy = "timestamp"
    search_fields = ["titulo", "descripcion"]
    list_display = ["titulo", "precio", "active", "updated"]
    list_editable = ["precio", "active"]
    list_filter = ["precio", "active"]
    readonly_fields = ["timestamp", "updated"]
    prepopulated_fields = {'slug': ["titulo"]}
    ordering = ["titulo"]
    
    class Meta:
        model = Producto


class ProductoImagenAdmin(admin.ModelAdmin):
    #search_fields = [""]
    raw_id_fields = ["producto"]
    list_display = ["producto",'imagen', "presentada", "miniatura", "active", "updated"]  
    list_editable = ["presentada", "miniatura", "active"]      
    list_filter = ["presentada", "miniatura", "active"]
    readonly_fields = ["updated"]

    class Meta:
        model = ProductoImagen


admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProductoImagen, ProductoImagenAdmin)
