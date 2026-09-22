from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #HTTP RESPONSE
    return HttpResponse("HOME")# Create your views here.

def contato(request):
    #HTTP RESPONSE
    return HttpResponse("Contato")

def sobre(request):
    #HTTP RESPONSE
    return HttpResponse("Sobre")
