import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EncuestaSerializer
from .models import Encuesta
from django.shortcuts import get_object_or_404, redirect

from .utils import createQuiz


@api_view(['GET', 'POST'])
def encuesta_api_view(request):
    if request.method == 'GET':
        encuestas = Encuesta.objects.all()
        encuestas_serializer = EncuestaSerializer(encuestas, many=True)
        return Response(encuestas_serializer.data)
    elif request.method == 'POST':
        encuesta_serializer = EncuestaSerializer(data=request.data)
        if encuesta_serializer.is_valid():
            encuesta_serializer.save()
            return Response(encuesta_serializer.data)
        return Response(encuesta_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def encuesta_detalle_api_view(request, pk=None):
    encuesta = Encuesta.objects.filter(id=pk).first()
    if encuesta:
        if request.method == 'GET':
            encuesta_serializer = EncuestaSerializer(encuesta)
            return Response(encuesta_serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            encuesta_serializer = EncuestaSerializer(encuesta, data=request.data)
            if encuesta_serializer.is_valid():
                encuesta_serializer.save()
                return Response(encuesta_serializer.data,status=status.HTTP_200_OK)
            return Response(encuesta_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            encuesta.delete()
            return Response({'message': 'Quiz deleted'})
    return Response({'message': 'There is no quiz with that id'}, status=status.HTTP_400_BAD_REQUEST)


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
