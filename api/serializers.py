from rest_framework import serializers
from students.models import Student
from teachers.models import Teachers
from accounts.models import user

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = user
        fields = "__all__"