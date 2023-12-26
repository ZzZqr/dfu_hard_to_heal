import time

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):

    return render(request, 'hello_azure/index.html')


@csrf_exempt
def predict(request):
    if request.method == 'POST':
        time.sleep(5)
        data = {'label': 0, 'probability': 0.55}
        return JsonResponse(data)
    else:
        return render(request, 'hello_azure/index.html')
