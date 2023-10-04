from django.conf import settings

from django.db import models

User = settings.AUTH_USER_MODEL

class UsuarioStripe(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    stripe_id = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Usuarios de Stripe"

    def __str__(self):
        return self.usuario.username
    


