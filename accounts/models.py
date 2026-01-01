from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class user(AbstractUser):
    User_type_choices = (
        ('admin' , 'Admin'),
        ('student' , 'Student'),
        ('teacher' , 'Teacher')
    )
    user_type = models.CharField(choices=User_type_choices,max_length=50)
    phone = models.CharField( max_length=20)

    def __str__(self):
        return f'{self.username} - {self.user_type}'
    