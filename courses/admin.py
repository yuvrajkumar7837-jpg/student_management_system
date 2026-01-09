from django.contrib import admin
from courses.models import *

# Register your models here.

admin.site.register([Department , Course ,Result])

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student' , 'course' , 'status' , 'marked_by')
