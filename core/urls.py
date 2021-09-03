from .view import estudiante, psicologo, general
from django.urls import path, include
from django.contrib.auth import views as auth_view

# from .api import api_addQuiz,

urlpatterns = [
    path('estudiante/', include((
        [
            path('home_estudiante/', estudiante.go_estudiante, name='go_estudiante'),
            path('quiz/<int:pk>/', estudiante.quiz_detail, name="quiz_detail"),

        ]))),
    path('psicologo/', include((
        [
            path('home_psicologo/', psicologo.go_psicologo, name='go_psicologo'),
            # path('encuesta/', psicologo.EncuestaListView.as_view(), name='encuesta'),
            path('encuesta/', psicologo.EncuestaListView.as_view(), name='encuesta'),
            # path('quiz/', psicologo.quiz, name='quiz'),
            # CRUD PARA ENCUESTAS
            path('encuesta/<int:pk>/', psicologo.encuesta_detail, name='encuesta_detalle'),
            path('encuesta/create/', psicologo.EncuestaCreateView.as_view(), name="encuesta_create"),
            path('encuesta/update/<int:pk>/', psicologo.EncuestaUpdateView.as_view(), name="encuesta_update"),
            path('encuesta/delete/<int:pk>/', psicologo.EncuestaDeleteView.as_view(), name="encuesta_delete"),
            # CRUD PARA PREGUNTAS
            path('pregunta/<int:pk>/', psicologo.pregunta_detail, name="pregunta_detalle"),
            path('pregunta/create/<int:pk>', psicologo.PreguntaCreateView.as_view(), name="pregunta_create"),
            path('pregunta/update/<int:pk>', psicologo.PreguntaUpdateView.as_view(), name="pregunta_update"),
            path('pregunta/delete/<int:pk>', psicologo.PreguntaDeleteView.as_view(), name="pregunta_delete"),
            # CRUD PARA OPCIONES
            path('opcion/create/<int:pk>', psicologo.OpcionCreateView.as_view(), name="opcion_create"),
            path('opcion/update/<int:pk>', psicologo.OpcionUpdateView.as_view(), name="opcion_update"),
            path('opcion/delete/<int:pk>', psicologo.OpcionDeleteView.as_view(), name="opcion_delete"),
            # CRUD PARA CATEGORIAS
            path('categoria/', psicologo.CategoriaListView.as_view(), name="categoria"),
            path('categoria/create/', psicologo.CategoriaCreateView.as_view(), name="categoria_create"),
            path('categoria/update/<int:pk>/', psicologo.CategoriaUpdateView.as_view(), name="categoria_update"),
            path('categoria/delete/<int:pk>/', psicologo.CategoriaDeleteView.as_view(), name="categoria_delete"),
            # CRUD PARA FORMULAS
            path('formula/', psicologo.FormulaListView.as_view(), name="formula"),
            path('formula/create/', psicologo.FormulaCreateView.as_view(), name="formula_create"),
            path('formula/update/<int:pk>', psicologo.FormulaUpdateView.as_view(), name="formula_update"),
            path('formula/delete/<int:pk>', psicologo.FormulaDeleteView.as_view(), name="formula_delete"),

            # CRUD PARA ESTUDIOS
            path('estudio/', psicologo.EstudioListView.as_view(), name="estudio"),
            path('estudio/create/', psicologo.EstudioCreateView.as_view(), name="estudio_create"),
            path('estudio/delete/<int:pk>/', psicologo.EstudioDeleteView.as_view(), name="estudio_delete"),
            # path('categoria/create/', psicologo.CategoriaCreateView.as_view(), name="categoria_create"),
            # path('categoria/update/<int:pk>/', psicologo.CategoriaUpdateView.as_view(), name="categoria_update"),
            # API

            # path('api/addQuiz', api_addQuiz, name='api_addQuiz'),
            # path('api/get_encuestas', encuesta_api_view, name='get_encuestas'),
            # path('api/get_encuesta/<int:pk>', encuesta_detalle_api_view, name="get_encuesta"),
            # path('api/get_preguntas/<int:fk>', preguntas_api_view, name="get_preguntas"),
        ]))),
    path('', general.login_general, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='core/logout.html'), name="logout"),

]
