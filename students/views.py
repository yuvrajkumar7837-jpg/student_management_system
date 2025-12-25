from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'students/index.html')

def t_login(request):
    return render(request , 'students/t_login.html')

def s_login(request):
    return render(request , 'students/s_login.html')