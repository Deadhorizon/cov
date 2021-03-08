from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import pandas as pd
import requests
# Create your views here.

@csrf_exempt
def covid_list(request):
    if request.method == 'GET':
      #content = requests.get().content
      df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-table-data.csv').transpose()
      df.to_json('E:\Project\Django\cov\snippets\data.json')
      content = pd.DataFrame.to_json(df)
      return JsonResponse(content,safe= False)
      