from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from core.models import user_type

def go_psicologo(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).es_psicologo:
        return render(request, 'core/Psicologo/homeP.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).es_estudiante:
        return redirect('go_estudiante')
    else:
        return redirect('login')


@login_required()
def profile_psicologo(request):
    return render(request, 'core/profile.html')