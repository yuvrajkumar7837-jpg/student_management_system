from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate , login
from django.http import HttpResponse

# Create your views here.

def t_login(request):
    if request.method == "post":
        username = request.post.get("username")
        password = request.post.get("password")

        user = authenticate(request , username = username , password = password)

        if user is not None:
            #check for teachers --
            if user.groups.filter(name = "teachers").exists():
                login(request , user)
                return redirect("teacher_dashboard")
            else:
                messages.error(request , 'You are not a teacher')
        else:
            messages.error('Invalid creditional')

    return render(request ,'teachers/login.html')





def teacher_dashboard(req):
    return HttpResponse('teacher dashbaord')

