from django.contrib import admin

from carro.models import Carro, CarroItem


class CarroItemInline(admin.StackedInline):
    model = CarroItem
    extra = 0
    readonly_fields = ["timestamp", "updated"]
    date_hierarchy = "timestamp"

class CarroAdmin(admin.ModelAdmin):   
    inlines = [CarroItemInline] 
    date_hierarchy = "timestamp"
    list_display = ["id","total", "activo"]
    list_editable = ["total", "activo"]
    list_filter = ["activo"]
    readonly_fields = ["timestamp", "updated"]

    class Meta:
        model: Carro


class CartItemAdmin(admin.ModelAdmin):
    date_hierarchy = "timestamp"
    list_editable = ["cantidad"]
    list_display = ["carro","producto","cantidad", "linea_total"]
    readonly_fields = ["timestamp", "updated"]

    class Meta:
        model: CarroItem

admin.site.register(Carro, CarroAdmin)
admin.site.register(CarroItem, CartItemAdmin)
