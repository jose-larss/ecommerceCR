from django.urls import path

from pedido.views import checkout, pedidos

app_name = "checkout"

urlpatterns = [
    path('', checkout,name="checkout"), 
    path('pedidos/', pedidos, name="user_orders"),
]