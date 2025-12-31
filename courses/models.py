from django.db import models
from teachers.models import Teachers
from students.models import students
# Create your models here.

class Department(models.Model):

    dep_name = models.CharField( max_length=50)
    dep_id = models.IntegerField()
    teacher = models.ForeignKey(Teachers,  on_delete=models.SET_NULL , null = True)
    students = models.ManyToManyField(students ,  blank= True)
    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class Attendance(models.Model):
    student = models.ForeignKey(students, on_delete=models.CASCADE)
    course = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    STATUS_CHOICES = (
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    marked_by = models.ForeignKey(Teachers, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        unique_together = ['student', 'course', 'date']
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.student} - {self.course} - {self.date}"

