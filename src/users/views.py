from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == "POST":
        # username = request.POST["login_username"]
        username = request.POST.get("login_username")
        password = request.POST.get("login_password")
        # possible_user = User.objects.filter(username=username, password=password)
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user and authenticated_user.is_active:
            django_login(request, authenticated_user)
            return redirect('home_page')
        else:
            messages.error(request, "Usuario incorrecto o inactivo")
            # print("Usuario incorrecto o inactivo")

    return render(request, "login_form.html")
    # Django busca las plantillas en todas las carpetas "templates" de las aplicaciones instaladas
    # (variable INSTALLED_APPS en "settings.py")
