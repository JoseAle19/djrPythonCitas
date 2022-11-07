from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def welcome(request):
    return HttpResponse('Hola, bienvenido, rest api citas kairo')