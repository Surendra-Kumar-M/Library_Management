from django.shortcuts import render
from django.http import HttpResponse
from .models import Books

# Create your views here.
def Home(request):
    return HttpResponse("Hello")

