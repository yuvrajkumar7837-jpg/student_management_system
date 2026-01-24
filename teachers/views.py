from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from courses.models import Course ,Attendance ,Department
from students.models import Student
from teachers.models import Teachers
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

# @login_required
# def mark_attendance(req):
#     if  not req.user.groups.filter(name = 'teachers').exists():
#         messages.error(req , 'Access Denied You are not a teacher')
#         return redirect('teacher_dashboard')
    
#     student = 
#     courses = Course.objects.all()

#     students = Student.objects.all()

#     if req.method =='POST':
#         course_code = req.POST.get('course')
#         course = Course.objects.get(id=course_code)
        
#         try:
#             teacher = Teachers.objects.get(user=req.user)
#         except Teachers.DoesNotExist:
#             messages.error(req, "Teacher profile missing")
#             return redirect("teacher_dashboard")

#         for student in students:
#             status = req.POST.get(f"Status_{student.id}")
#             Attendance.objects.create(
#         ect("teacher_dashboard")

#     # return render(req, "attendance/mark_attendance.html", {
#     #     "courses": courses,
#     #     "students": students        student=student,
#                 course=course,
#                 status=status,
#                 marked_by = teacher
#             )

#         messages.success(req, "Attendance marked successfully")
#         return redir
#     # })


def mark_attendance(request):
    #check for teacher or not
    # if  not req.user.groups.filter(name = 'teachers').exists():
#         messages.error(req , 'Access Denied You are not a teacher')
#         return redirect('teacher_dashboard')
    
    if not request.user.groups.filter(name = 'teachers').exists():
        messages.error(request ,'You are not a Teacher')
        return redirect('teacher_dashboard')
    
    department = Department.objects.all()
    courses = []
    students = []
    
    selected_department = None


    selected_dept_id = request.POST.get('department')
    selected_course_id = request.POST.get('course')
    action = request.POST.get('action')


    if selected_dept_id:
        courses = Course.objects.filter(department_id=selected_dept_id)
    
    if action == 'load_students' and selected_course_id :
        course = Course.objects.get(id = selected_course_id)
        students = Student.objects.filter(department= course.department)

    if action == 'save_attendance' and selected_course_id:
            try: 
                teacher = Teachers.objects.get(user=request.user)
            except Teachers.DoesNotExist:
                messages.error(request, "Teacher profile missing")
                return redirect("teacher_dashboard")
            course = Course.objects.get(id=selected_course_id)
            teacher = Teachers.objects.get(user=request.user)

            students = Student.objects.filter(department=course.department)
            for student in students:
                status = request.POST.get(f"status_{student.id}")

                Attendance.objects.update_or_create(
                    student=student,
                    course=course,
                    status=status,
                    marked_by=teacher
                )

            messages.success(request, "Attendance saved successfully ✅")
            return redirect("mark_attendance") 


   
   

    return render(request , 'teachers/attendance.html' , {'departments' : department , 'courses': courses , 'selected_department':selected_dept_id  , 'students':students , 'selected_course_id':selected_course_id})

