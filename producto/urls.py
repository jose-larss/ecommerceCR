from django.urls import path

from producto.views import all_products, single

app_name = "producto"

urlpatterns = [
    path('', all_products, name="all"),
    path('<slug:slug>/', single, name="single_producto"),
]