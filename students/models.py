from django.db import models
from accounts.models import user

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    s_id      = models.IntegerField(unique=True )
    # passw = models.IntegerField(default=12)
    email =   models.EmailField(unique= True)
    phone_no = models.CharField(max_length=15)
    d_o_b = models.DateField(null= True)
    enrollement_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.s_id} : {self.first_name} {self.last_name}'
    

