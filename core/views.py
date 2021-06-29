from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import UserModel

def inicio(request):
    if request.method == "POST":
        email = request.POST.get('email')
        contrasenia = request.POST.get('password')
        username = UserModel.objects.get(email=email.lower()).username
        user = authenticate(username=username, password=contrasenia)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,'Usuario o Contraseña Incorrecta')
    return render(request,'core/login.html')

def home(request):
    return render(request, 'core/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'core/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'core/profile.html')