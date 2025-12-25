from django.urls import path
from teachers import views
urlpatterns = [
    path('login/' , views.t_login ,  name = 't_login')
]
