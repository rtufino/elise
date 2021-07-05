from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import UserModel
from ..decorators import estudiante_required

def inicio(request):
    if request.method == "POST":
        email = request.POST.get('email')
        contrasenia = request.POST.get('password')
        username = UserModel.objects.get(email=email.lower()).username
        user = authenticate(username=username, password=contrasenia)
        print("asdas"+email)

        if user is not None:
            login(request,user)
            print(email)
            return redirect('profile')
        else:
            messages.warning(request,'Usuario o Contraseña Incorrecta')
    context= {}
    return render(request,'core/login.html',context)

def home(request):
    return render(request, 'core/Estudiante/home.html')


@login_required()
def profile(request):
    return render(request, 'core/profile.html')