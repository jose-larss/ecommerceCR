from django.urls import path

from carro.views import (vista, 
                         add_to_cart, 
                         borrar_carro, 
                         update_to_quantity,
                         borrar_item_carro)

app_name = "carro"

urlpatterns = [
    
    path('', vista, name="vista"),
    #path('<str:url>/', vista, name="vista_con_parametro"),
    path('actualizar_cantidad/',update_to_quantity, name="update_to_quantity"),
    path('<slug:slug>/',add_to_cart, name="update_to_cart"),
    path('delete_item/<int:item_carroid>/', borrar_item_carro, name="borrar_item_carro"),
    path('delete/', borrar_carro, name="borrar_carro"),
    
]