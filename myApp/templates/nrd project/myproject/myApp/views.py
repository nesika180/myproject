from django.shortcuts import render
from django.http import HttpResponse

def details(request):
    return HttpResponse("now your in django page")
def screen(request):
    return HttpResponse("now your in output Screen")

def index(request):
     return render(request,"index.html")