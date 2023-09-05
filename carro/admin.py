from django.contrib import admin

from carro.models import Carro

class CarroAdmin(admin.ModelAdmin):
    date_hierarchy = "timestamp"
    list_display = ["id","total", "activo"]
    list_editable = ["total", "activo"]
    list_filter = ["activo"]
    readonly_fields = ["timestamp", "updated"]

    class Meta:
        model: Carro

admin.site.register(Carro, CarroAdmin)
