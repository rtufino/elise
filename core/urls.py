from django.urls import include, path
from .view import estudiante,psicologo,general
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('estudiante/', include((
        [
            path('home_estudiante/', estudiante.go_estudiante, name='go_estudiante'),

        ]))),
    path('psicologo/', include((
        [
            path('home_psicologo/', psicologo.go_psicologo, name='go_psicologo'),

        ]))),
    path('', general.login_general, name='login'),
    path('profile/', general.profile, name='profile'),
    path('logout/', auth_view.LogoutView.as_view(template_name='core/logout.html'), name="logout"),

]