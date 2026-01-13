from django.contrib import admin
from courses.models import *

# Register your models here.

admin.site.register([ Result , ])

class CourseAdmin(admin.ModelAdmin):
    list_display = ( 'department' ,  'course_name' , 'course_code')

admin.site.register(Course , CourseAdmin)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('date','student' , 'course' , 'status' , 'marked_by')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dep_name', 'hod')
