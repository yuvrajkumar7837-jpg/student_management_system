from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from students.models import Student
from courses.models import Course



# Create your views here.

def home(request):
    return render(request, 'students/index.html')

def t_login(request):
    return render(request , 'teachers/t_login.html')

def s_login(request):
    if request.method == "POST":
        username = request.POST.get("username")  # or username field
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # check student role
            if user.groups.filter(name="students").exists():
                login(request, user)
                return redirect("student_dashboard")
            else:
                messages.error(request, "You are not a student")
        else:
            messages.error(request, "Invalid credentials")


    return render(request , 'students/s_login.html')



@login_required
def student_dashboard(request):
    student = Student.objects.get(user = request.user)

    courses = Course.objects.filter(department = student.department)


    return render(request , 'students/dashboard.html' , {'student':student , 'courses' : courses})
    # return render(request, "students/dashboard.html")


def show_courses(req):
    student = Student.objects.get(user = req.user)

    courses = Course.objects.filter(department = student.department)
    return render(req , 'students/courses.html', {'student':student , 'courses' : courses})


def logout_view(request):
    logout(request)
    return redirect('/')
    