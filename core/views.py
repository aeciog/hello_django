from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(requests,nome):
    return HttpResponse(f'<h1> Hello {nome} </h1>')