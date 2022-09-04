from django.http import HttpResponse
from django.shortcuts import render

def start(request):
    return render(request, 'start.html')

def reverse(request):
    return render(request, 'reverse.html')