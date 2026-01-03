from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponse

# Create your views here.

def t_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request , username = username , password = password)

        if user is not None:
            #check for teachers --
            if user.groups.filter(name = "teachers").exists():
                login(request , user)
                # messages.success(request , 'congrtulations')
                return redirect("teacher_dashboard")
            else:
                messages.error(request , 'You are not a teacher')
        else:
            messages.error('Invalid creditional')

    return render(request ,'teachers/login.html')




@login_required
def teacher_dashboard(req):
   return render(req,'teachers/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('/')
