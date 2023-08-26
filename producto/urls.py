from django.urls import path

from producto.views import all_products

app_name = "producto"

urlpatterns = [
    path('', all_products, name="all"),
]