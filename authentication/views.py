import json

from django.contrib.auth import authenticate, forms
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method == 'GET':
        user = authenticate(request, username=request.GET.get('username'), password=request.GET.get('password'))

        if user is not None:
            return HttpResponse(json.dumps({'username': str(user)}), content_type='application/json')

        return JsonResponse({'status': 10, 'text': 'The attributes have not been provided properly!'})

    return JsonResponse({'status': 11, 'text': 'This method processes only POST requests!'})