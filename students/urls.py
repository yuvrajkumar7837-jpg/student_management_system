from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('' , views.home , name='home'),
    path('login/' , views.s_login , name='s_login'),
    path('teacher_login' , views.t_login , name='t_login'),
    path("dashboard/", views.student_dashboard, name="student_dashboard"),
    path("courses/", views.show_courses, name="courses"),
    path("logout/" , views.logout_view , name = 'logout')


]

     