from django.db import models

# Create your models here.

class students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    s_id      = models.IntegerField()
    passw = models.IntegerField(default=12)
    email =   models.EmailField()
    phone_no = models.CharField(max_length=15)
    d_o_b = models.DateField()
    enrollement_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

