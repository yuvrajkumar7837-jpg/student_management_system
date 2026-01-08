from django.db import models
from teachers.models import Teachers
from students.models import Student
from django.contrib.auth.models import AbstractUser # for imporrting built in models
# Create your models here.

class Department(models.Model):
    STATUS_CHOICES = (
        ('B.tech', 'B.tech'),
        ('B.com', 'B.com'),
        ('B.A', 'B.A'),
    )

    DEP_ID_CHOICES = (
        (1, 'B.tech'),
        (2, 'B.com'),
        (3, 'B.A'),
    )
    

    dep_name = models.CharField( max_length=50 , choices=STATUS_CHOICES)
    dep_id = models.IntegerField(choices=DEP_ID_CHOICES)
    teacher = models.ForeignKey(Teachers,  on_delete=models.SET_NULL , null = True)
    students = models.ManyToManyField(Student ,  blank= True)
    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return f"{self.dep_id} - {self.dep_name}"
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})




class Course(models.Model):  # ✅ Added separate Course model
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student, blank=True)
    
    def __str__(self):
        return f"{self.course_code} - {self.course_name}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null= True)
    marked_by = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.student} - {self.course} - {self.date}"
    
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Department, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=50)  # Midterm, Final, Quiz
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)
    exam_date = models.DateField()
    created_by = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-exam_date']
    
    def percentage(self):
        return (self.marks_obtained / self.total_marks) * 100
    
    def __str__(self):
        return f"{self.student} - {self.course} - {self.exam_type}"

