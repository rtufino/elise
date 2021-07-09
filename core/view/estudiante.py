from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from core.models import user_type

def go_estudiante(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).es_estudiante:
        return render(request, 'core/Estudiante/home.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).es_psicologo:
        return redirect('go_psicologo')
    else:
        return redirect('login')

@login_required()
def profile_estudiante(request):
    return render(request, 'core/profile.html')