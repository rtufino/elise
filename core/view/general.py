from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from core.models import user_type
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_general(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.es_estudiante:
                return redirect('go_estudiante')
            elif user.is_authenticated and type_obj.es_psicologo:
                return redirect('go_psicologo')
        else:
            messages.warning(request, 'Usuario o Contraseña Incorrecta')
            return redirect('login')

    return render(request, 'core/login.html')
