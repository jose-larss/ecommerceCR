from django.urls import path

from carro.views import vista, update_to_cart, borrar_carro

app_name = "carro"

urlpatterns = [
    path('', vista, name="vista"),
    path('delete/', borrar_carro, name="borrar-carro"),
    path('<slug:slug>/',update_to_cart, name="update_to_cart"),
]