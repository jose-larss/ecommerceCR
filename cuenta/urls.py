from django.urls import path

from cuenta.views import logout_view

app_name = "cuentas"

urlpatterns = [
    path('logout/',logout_view, name="auth_logout"),
]