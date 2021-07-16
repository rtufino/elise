from django.urls import include, path
from .view import estudiante, psicologo, general
from django.urls import path, include
from django.contrib.auth import views as auth_view

from .api import api_addQuiz, encuesta_api_view, encuesta_detalle_api_view

urlpatterns = [
    path('estudiante/', include((
        [
            path('home_estudiante/', estudiante.go_estudiante, name='go_estudiante'),

        ]))),
    path('psicologo/', include((
        [
            path('home_psicologo/', psicologo.go_psicologo, name='go_psicologo'),
            path('quiz/', psicologo.quiz, name='quiz'),

            # API

            path('api/addQuiz', api_addQuiz, name='api_addQuiz'),
            path('api/get_encuestas', encuesta_api_view, name='get_encuestas'),
            path('api/get_encuesta/<int:pk>', encuesta_detalle_api_view, name="get_encuesta")
        ]))),
    path('', general.login_general, name='login'),
    path('profile/', general.profile, name='profile'),
    path('logout/', auth_view.LogoutView.as_view(template_name='core/logout.html'), name="logout"),

]