from django.conf import settings

from django.db import models

User = settings.AUTH_USER_MODEL

class UsuarioStripe(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Usuarios de Stripe"

    def _str__(self):
        return self.stripe_id
    


