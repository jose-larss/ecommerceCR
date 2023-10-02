import stripe

from django.conf import settings
from django.contrib.auth.signals import user_logged_in

from cuenta.models import UsuarioStripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def get_or_create_stripe(sender, user, *args, **kwargs):
    try: 
        user.usuariostripe.stripe_id
    except UsuarioStripe.DoesNotExist:
        customer = stripe.Customer.create(
            email = str(user.email)
        )
        new_user_stripe = UsuarioStripe.objects.create(
            usuario = user,
            stripe_id = customer.id
        )
        print(new_user_stripe)
user_logged_in.connect(get_or_create_stripe)