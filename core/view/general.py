from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_general(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_authenticated and user.is_active and not user.is_staff:
                return redirect('go_estudiante')
            elif user.is_authenticated and user.is_active and user.is_staff:
                return redirect('go_psicologo')
        else:
            messages.warning(request, 'Usuario o Contraseña Incorrecta')
            return redirect('login')
    return render(request, 'core/login.html')
