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
        time.sleep(3)

        probability = 0.1

        age = int(request.POST.get('Age'))

        if age == 10:
            probability = 0.10
        elif age == 20:
            probability = 0.20
        elif age == 30:
            probability = 0.50
        elif age == 40:
            probability = 0.70
        elif age == 50:
            probability = 0.90

        data = {'label': 0, 'probability': probability}
        return JsonResponse(data)
    else:
        return render(request, 'hello_azure/index.html')
