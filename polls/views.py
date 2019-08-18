from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import generics
from polls.serializers import CitizenSerializer
import json
import requests    
from polls.models import *

def index(request):
	return HttpResponse('Hello, my friend')

# class CitizenCreateView()

@api_view(['POST'])
def imports(request):
	data = json.loads(request.body)
	ls = ''   
	f =[]
	for i in data:
		f = (Citizen(citizen_id = int(i['citizen_id']) , town = i['town']))  
		f.save()
		ls += i['town'] 
	return HttpResponse(ls)