from django.urls import path

from carro.views import (vista, 
                         add_to_cart, 
                         borrar_carro, 
                         update_to_quantity,
                         borrar_item_carro)

app_name = "carro"

urlpatterns = [
    
    path('', vista, name="vista"),
    path('actualizar_cantidad/',update_to_quantity, name="update_to_quantity"),
    path('delete/', borrar_carro, name="borrar_carro"),
    path('<slug:slug>/',add_to_cart, name="update_to_cart"),
    path('delete_item/<int:item_carroid>/', borrar_item_carro, name="borrar_item_carro"),
   
    
]