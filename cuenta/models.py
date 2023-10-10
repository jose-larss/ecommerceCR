from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models

User = settings.AUTH_USER_MODEL

"""
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] #estos campos son requeridos a la hora de crear un usuario por consola
"""




class UsuarioStripe(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    stripe_id = models.CharField(max_length=120)
    fecha_nacimiento = models.DateField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Usuarios de Stripe"

    def __str__(self):
        return self.usuario.username
    


