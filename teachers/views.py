from django.shortcuts import render

# Create your views here.

def t_login(req):
    return render(req ,'teachers/login.html')

