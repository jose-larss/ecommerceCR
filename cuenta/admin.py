from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from cuenta.models import UsuarioStripe

#User = settings.AUTH_USER_MODEL

#class UsuarioStripeAdmin(admin.ModelAdmin):
#    list_display = ["usuario", "stripe_id"]


class UsuarioStripeInline(admin.StackedInline):
    model = UsuarioStripe
    extra = 0


class UserAdmin(BaseUserAdmin):
    inlines = [UsuarioStripeInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
