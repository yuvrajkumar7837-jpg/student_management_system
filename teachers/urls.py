from django.urls import path
from teachers import views
urlpatterns = [
    path('login/' , views.t_login ,  name = 't_login'),
    path("teacher_dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
]
