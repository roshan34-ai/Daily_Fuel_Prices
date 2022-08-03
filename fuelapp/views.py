from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from django.http.response import JsonResponse
import json, requests


# Create your views here.

@api_view(['GET'])
def Petrol_Prices(request):
    India_url = 'https://economictimes.indiatimes.com/wealth/fuel-price/petrol'

    source = requests.get(India_url)
    soup = BeautifulSoup(source.text, 'lxml')

    data = []
    table = soup.find('tbody')
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    d1 = {}
    for i in range(len(data)):
        d1.update({data[i][0]:data[i][1].replace('\u20b9','')})

    return JsonResponse(
        {"petrol prices today":d1},
        safe=False)  
   

@api_view(['GET'])
def Diesel_Prices(request):
    India_url = 'https://economictimes.indiatimes.com/wealth/fuel-price/diesel'

    source = requests.get(India_url)
    soup = BeautifulSoup(source.text, 'lxml')
    
    data = []
    table = soup.find('tbody')
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    d1 = {}
    for i in range(len(data)):
        d1.update({data[i][0]:data[i][1].replace('\u20b9','')})

    return JsonResponse({
        "diesel prices today":d1},
        safe=False)  
   

@api_view(['GET'])
def LPG_Prices(request):
    India_url = 'https://www.goodreturns.in/lpg-price.html'

    source = requests.get(India_url)
    soup = BeautifulSoup(source.text, 'lxml')
    
    data = []
    table = soup.find("div", class_="gold_silver_table")
  
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    del data[0]
    d1 = {}
    for i in range(len(data)):
        d1.update({data[i][0]:data[i][1].replace('\u20b9','')})

    return JsonResponse({
        "LPG prices today":d1},
        safe=False)  

@api_view(['GET'])
def CNG_Prices(request):
    India_url = 'https://www.goodreturns.in/cng-price.html'

    source = requests.get(India_url)
    soup = BeautifulSoup(source.text, 'lxml')
    
    data = []
    table = soup.find("div", class_="gold_silver_table")
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    del data[0]
    d1 = {}
    for i in range(len(data)):
        d1.update({data[i][0]:data[i][1].replace('\u20b9','')})

    return JsonResponse({
        "CNG prices today":d1},
        safe=False)  
