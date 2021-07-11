import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EncuestaSerializer
from .models import Encuesta
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from .utils import createQuiz

class EncuestaApiView(APIView):
    def get(self, request):
        encuestas= Encuesta.objects.all()
        encuestas_serializer = EncuestaSerializer(encuestas, many=True)
        return Response(encuestas_serializer.data)

def api_addQuiz(request):
    data = json.loads(request.body)
    jsonresponse = {'success', True}
    name = data['name']
    state = data['state']
    vig_date = data['vig_date']
    type = data['type']
    start_date = data['start_date']

    quiz_id = createQuiz(request, name, state, vig_date, type, start_date)
    return redirect('/')


