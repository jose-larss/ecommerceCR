from django.urls import path

from carro.views import vista

app_name = "carro"

urlpatterns = [
    path('', vista, name="vista")
]