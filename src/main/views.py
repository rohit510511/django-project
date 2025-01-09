from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def landing_vie(request):
    return HttpResponse("<h1>Welcome to Automax!!</h1>")