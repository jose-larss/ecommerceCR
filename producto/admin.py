from django.contrib import admin

from producto.models import Producto, ProductoImagen, Categoria, Variacion

class CategoriaAdmin(admin.ModelAdmin):
    date_hierarchy = "timestamp"
    search_fields = ["titulo", "descripcion"]
    list_display = ["id","titulo", "presentada", "active"]
    list_editable = ["presentada", "active"]
    list_filter = ["active"]
    readonly_fields = ["timestamp", "updated"]
    prepopulated_fields = {'slug':["titulo"]}
    ordering = ["titulo"]

    class Meta:
        model = Categoria
"""
class ProductoImagenAdmin(admin.ModelAdmin):
    #search_fields = [""]
    raw_id_fields = ["producto"]
    list_display = ["producto",'imagen', "presentada", "miniatura", "active", "updated"]  
    list_editable = ["presentada", "miniatura", "active"]      
    list_filter = ["presentada", "miniatura", "active"]
    readonly_fields = ["updated"]

    class Meta:
        model = ProductoImagen
"""

class VariacionInlines(admin.TabularInline):
    model = Variacion
    extra = 0
    readonly_fields = ["updated"]

class ProductoImagenInline(admin.TabularInline):
    model = ProductoImagen
    extra = 0
    readonly_fields = ["updated"]

class ProductoAdmin(admin.ModelAdmin):
    inlines = [ProductoImagenInline, VariacionInlines]
    date_hierarchy = "timestamp"
    search_fields = ["titulo", "descripcion"]
    list_display = ["titulo", "color","precio", "active", "updated"]
    list_editable = ["precio", "active"]
    list_filter = ["categoria","precio", "active"]
    readonly_fields = ["timestamp", "updated"]
    prepopulated_fields = {'slug': ["titulo", "color"]}
    ordering = ["titulo"]
    
    class Meta:
        model = Producto

class VariacionAdmin(admin.ModelAdmin):
    list_display = ["producto", "variacion","imagen","titulo","precio", "active"]
    list_editable = ["precio","imagen", "titulo", "precio","active"]
    list_filter = ["producto"]
    readonly_fields = ["updated"]
    ordering = ["producto"]

    class Meta:
        model = Variacion


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Variacion, VariacionAdmin)
#admin.site.register(ProductoImagen, ProductoImagenAdmin)
