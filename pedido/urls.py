from django.urls import path

from pedido.views import pedido

app_name = "pedido"

urlpatterns = [
    path('', pedido,name="vista"), 
]