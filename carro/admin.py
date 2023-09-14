from django.contrib import admin

from carro.models import Carro, CarroItem

class CarroAdmin(admin.ModelAdmin):
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
