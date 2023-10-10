from django.urls import path

from cuenta.views import (logout_view, 
                          login_view, 
                          register_view,
                          register_partial_view,
                          login_partial_view)

app_name = "cuentas"

urlpatterns = [
    path('logout/',logout_view, name="auth_logout"),
    path('login/', login_view, name="auth_login"),
    path('register/', register_view, name="auth_register"),
    #parciales de login y register
    path('login/partial/', login_partial_view, name="auth_login_partial"),
    path('register/partial/', register_partial_view, name="auth_register_partial"),
]