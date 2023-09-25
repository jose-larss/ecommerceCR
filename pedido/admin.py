from django.contrib import admin

from pedido.models import Pedido

class PedidoAdmin(admin.ModelAdmin):
    
    date_hierarchy = "timestamp"
    search_fields = ["pedido_id", "carro"]
    list_display = ["pedido_id", "carro", "estado", "updated"]
    readonly_fields = ["timestamp", "updated"]
    list_filter = ["estado"]
    list_editable = ["carro","estado"]
    ordering = ["pedido_id"]

    class Meta:
        model= Pedido

admin.site.register(Pedido, PedidoAdmin)
