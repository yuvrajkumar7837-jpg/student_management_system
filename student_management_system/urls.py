"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from students import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.home , name ='home'),
    path('students/' , include('students.urls')),
    path('teachers/' , include('teachers.urls')),
    path('api/v1/' , include('api.urls')),
    # path("logout/", LogoutView.as_view(), name="logout"),

    # path('teacher_login/' , views.t_login , name='t_login'),
    # path('student_login/' , views.s_login , name='s_login'),
]
