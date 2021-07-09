from .models import Encuesta

def createQuiz(request, name, state, vig_date, type, start_date):
    quiz = Encuesta(nombre=name, estado=state, f_vigencia=vig_date, tipo=type, f_inicio=start_date)
    quiz.save()
    return quiz.id

