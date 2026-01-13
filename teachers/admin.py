from django.contrib import admin
from teachers.models import Teachers

# Register your models here.
@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('t_id','first_name' , 'email')
