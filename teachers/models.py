from django.db import models
from accounts.models import user
from django.conf import settings

# Create your models here.
class Teachers(models.Model):
    user  = models.OneToOneField(  settings.AUTH_USER_MODEL,user, on_delete=models.CASCADE)
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    t_id = models.CharField(max_length=50 , unique= True)
    # passw = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)
    enrollment_date = models.DateField(auto_now_add= True)

    def __str__(self):
        return f'{self.t_id} : {self.first_name} {self.last_name}'
