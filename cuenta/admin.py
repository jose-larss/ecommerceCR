from django.contrib import admin

from cuenta.models import UsuarioStripe

class UsuarioStripeAdmin(admin.ModelAdmin):
    list_display = ["usuario", "stripe_id"]

admin.site.register(UsuarioStripe, UsuarioStripeAdmin)
