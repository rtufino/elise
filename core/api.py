import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from .utils import createQuiz

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


