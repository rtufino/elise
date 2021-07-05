from django.urls import include, path
from .view import estudiante,psicologo
from django.contrib.auth import views as auth_view

# urlpatterns = [
#     path('', views.inicio, name="login"),
#     path('home/', views.home, name='home'),
#     path('profile/', views.profile, name='profile'),
#     path('logout/', auth_view.LogoutView.as_view(template_name='core/logout.html'), name="logout"),
# ]
urlpatterns = [
    path('estudiante/', include((
        [
            path('', estudiante.inicio, name='login'),
            path('profile/', estudiante.profile, name='profile'),
            path('logout/', auth_view.LogoutView.as_view(template_name='core/logout.html'), name="logout"),
        ]))),
    path('psicologo/', include((
        [
            # path('', psicologo.inicio, name='login'),
            path('profile/', psicologo.profile, name='profile'),
            path('logout/', auth_view.LogoutView.as_view(template_name='core/logout.html'), name="logout"),
        ]))),

]