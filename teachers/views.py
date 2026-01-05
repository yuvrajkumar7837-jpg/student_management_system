from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from courses.models import Course ,Attendance
from students.models import Student

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
            messages.error(request , 'Invalid creditional')

    return render(request ,'teachers/login.html')


@login_required
def teacher_dashboard(req):
   return render(req,'teachers/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def mark_attendance(req):
    if  not req.user.groups.filter(name = 'teachers').exists():
        messages.error(req , 'Access Denied You sre not a teacher')
        return redirect('teacher_dashboard')
    
    courses = Course.objects.all()

    students = Student.objects.all()

    if req.method =='POST':
        course_id = req.POST.get('course')
        for student in students:
            status = req.POST.get(f"status_{student.id}")
            Attendance.objects.create(
                student=student,
                course_id=course_id,
                status=status
            )

        messages.success(req, "Attendance marked successfully")
        return redirect("teacher_dashboard")

    # return render(req, "attendance/mark_attendance.html", {
    #     "courses": courses,
    #     "students": students
    # })

    return render(req , 'teachers/attendance.html' , {"courses" : courses , "students" : students})
    

