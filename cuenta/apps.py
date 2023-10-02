from django.apps import AppConfig


class CuentaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cuenta'

    def ready(self):
        from cuenta import signals
