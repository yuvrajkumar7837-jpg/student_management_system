from django.db import models

# Create your models here.
class Teachers(models.Model):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    t_id = models.CharField(max_length=50)
    passw = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField()
    enrollment_date = models.DateField(auto_now_add= True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
print('hello')