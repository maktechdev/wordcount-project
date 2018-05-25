from django.http import HttpResponse
from datetime import datetime as dt
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'time':dt.today()})

def count(request):
    return render(request, 'count.html', {'time':dt.today()})
