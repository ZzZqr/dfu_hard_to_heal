import time

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        data = {
            "Inputs": {
                "input1":
                    [
                        {  
                            'Sex': request.POST.get('input1Gender'),   
                            'Use_of_insulin': request.POST.get('input1Insulin'),   
                            'Random_blood_glucose': request.POST.get('input1BloodGlucose'),  
                            'CRP': request.POST.get('input1CRP'),  
                            'Wound_area': request.POST.get('input1WoundArea'),   
                            'Retinopathy': request.POST.get('input1Retinopathy'),   
                            'peripheral_arterial_disease': request.POST.get('input1Disease'),   
                            'Smoking_history': request.POST.get('input1SmokingHistory'),   
                            'Albumin': request.POST.get('input1Albumin'),   
                            'Creatinine': request.POST.get('input1Creatinine'),
                        }
                    ],
                },
            "GlobalParameters":  {
            }
        }
        print(data)

        body = str.encode(json.dumps(data))

        time.sleep(5)

        return render(request, 'hello_azure/index.html', {'label': 0,
                                                          'probability': 0.55})

        # url = 'https://ussouthcentral.services.azureml.net/workspaces/dba19b2bcf0e4a738568e2eb878d6582/services/d71570b4564a4d6a84a3a4153ad005dc/execute?api-version=2.0&format=swagger'
        # api_key = 'Ev/d720zxLMY+POUcSF0Kuib5uw0fdcLLQgXha9qD6rLxXUsT2yJ+lu7VUJnRu4j7/+FHnSTJqPOIydjLHEu4Q==' # Replace this with the API key for the web service
        # headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
        #
        # req = urllib.request.Request(url, body, headers)
        #
        # try:
        #     response = urllib.request.urlopen(req)
        #
        #     result = response.read()
        #     print(result)
        # except urllib.error.HTTPError as error:
        #     print("The request failed with status code: " + str(error.code))
        #
        #     # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        #     print(error.info())
        #     print(json.loads(error.read().decode("utf8", 'ignore')))
        # dict = eval(urllib.request.urlopen(req).read().decode())
        # return render(request, 'hello_azure/index.html',{'label':dict['Results']['output1'][0]['Scored Labels'],'probability': dict['Results']['output1'][0]['Scored Probabilities']})
    else:
        return render(request, 'hello_azure/index.html')

@csrf_exempt
def predict(request):
    return render(request, 'hello_azure/index.html')
    # if request.method == 'POST':
    #     data = {
    #             "Inputs": {
    #                     "input1":
    #                     [
    #                         {
    #                                 'Age': "1",
    #                                 'Sex': "1",
    #                                 'Use_of_insulin': "1",
    #                                 'Random_blood_glucose': "1",
    #                                 'Column 4': "1",
    #                                 'Wound_area': "1",
    #                                 'Retinopathy': "1",
    #                                 'peripheral_arterial_disease': "1",
    #                                 'Smoking_history': "1",
    #                                 'Albumin': "1",
    #                                 'Creatinine': "1",
    #                         }
    #                     ],
    #             },
    #         "GlobalParameters":  {
    #         }
    #     }
    #
    #     body = str.encode(json.dumps(data))
    #
    #     url = 'https://ussouthcentral.services.azureml.net/workspaces/dba19b2bcf0e4a738568e2eb878d6582/services/d71570b4564a4d6a84a3a4153ad005dc/execute?api-version=2.0&format=swagger'
    #     api_key = 'Ev/d720zxLMY+POUcSF0Kuib5uw0fdcLLQgXha9qD6rLxXUsT2yJ+lu7VUJnRu4j7/+FHnSTJqPOIydjLHEu4Q==' # Replace this with the API key for the web service
    #     headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    #
    #     req = urllib.request.Request(url, body, headers)
    #
    #     try:
    #         response = urllib.request.urlopen(req)
    #
    #         result = response.read()
    #         print(result)
    #     except urllib.error.HTTPError as error:
    #         print("The request failed with status code: " + str(error.code))
    #
    #         # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    #         print(error.info())
    #         print(json.loads(error.read().decode("utf8", 'ignore')))
    #
    # else:
    #     return render(request, 'hello_azure/index.html')