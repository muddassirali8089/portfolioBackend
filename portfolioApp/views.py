from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from portfolioApp!")


def contact(request):
    return HttpResponse("this is contact...! project uploaded")

