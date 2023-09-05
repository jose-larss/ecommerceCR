from django.shortcuts import render

from carro.models import Carro

def vista(request):
    carro = Carro.objects.all()[0]

    context = {
        "carro": carro
    }
    return render(request, "carros/vista.html", context)
