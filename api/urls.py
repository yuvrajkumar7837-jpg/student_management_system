from django.urls import path , include
from api import views


urlpatterns = [
    path("" , views.student_data ,name= 'data'),
    path("teachers" , views.Teachers_data.as_view() ,name= 'teachers_data'),
    path("student/<int:pk>/" , views.single_data ,name= 'single_data'),
    path("teacher/<int:pk>/" , views.teacher_detail.as_view() ,name= 'teacher_single_data'),
    path("user/" , views.user_data.as_view(), name = 'user'),
    path("user/<int:pk>/" , views.single_user.as_view() , name = 'single_user')
]

