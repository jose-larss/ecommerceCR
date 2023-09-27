from django.contrib import admin

from pedido.models import Pedido

class PedidoAdmin(admin.ModelAdmin):
    
    date_hierarchy = "timestamp"
    search_fields = ["pedido_id", "carro"]
    list_display = ["id","pedido_id","usuario", "carro", "estado","sub_total", "tax_total", "final_total","updated"]
    readonly_fields = ["timestamp", "updated"]
    list_filter = ["estado"]
    list_editable = ["carro","estado", "sub_total", "tax_total", "final_total"]
    ordering = ["-carro"]

    class Meta:
        model= Pedido

admin.site.register(Pedido, PedidoAdmin)
