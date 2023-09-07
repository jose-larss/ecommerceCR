from django.urls import path

from carro.views import vista, update_to_cart

app_name = "carro"

urlpatterns = [
    path('', vista, name="vista"),
    path('<slug:slug>/',update_to_cart, name="update_to_cart"),
]