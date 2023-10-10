from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

from cuenta.models import UsuarioStripe
from cuenta.forms import RegistrationForm
from cuenta.forms import LoginForm


def logout_view(request):
    logout(request)
    return redirect("all_products")


def register_partial_view(request):
    return render(request, "cuentas/partials/register_partial.html")


def login_partial_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=email, password= password)
        print(user)
        login(request, user)
        #return redirect("all_products")    
    return render(request, "cuentas/partials/login_partial.html", {"form":form})


def register_view(request):
    form= RegistrationForm(request.POST or None)
    if form.is_valid():
        fecha = form.cleaned_data.get('fechaNac')
        #password1 = form.cleaned_data.get('password1')
        new_user = form.save()
        
        new_user_stripe = UsuarioStripe.objects.create(
            usuario= new_user,
            fecha_nacimiento = fecha
        )

        #new_user.set_password(password1)
    
        #return redirect("cuentas:auth_login")
    return render(request, "cuentas/register.html",{"form":form})


def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=email, password= password)
        print(user)
        login(request, user)
        #return redirect("all_products")


    return render(request,"cuentas/login.html", {"form":form})