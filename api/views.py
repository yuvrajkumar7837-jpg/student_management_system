from django.shortcuts import render
from students.models import Student
from django.http import JsonResponse ,HttpResponse ,Http404
from api import serializers
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from teachers.models import Teachers
from rest_framework import mixins , generics
from accounts.models import user
# Create your views here.

@api_view(['GET' , 'POST'])
def student_data(request):
    if request.method == 'GET':
        students = Student.objects.all()
        #withoout drf :
        # data = list(students.values())
        # return JsonResponse(data , safe=False)

        #with drf :
        serializer = serializers.StudentSerializer(students ,many = True)
        return Response(serializer.data ,status=status.HTTP_200_OK )
    
    elif request.method == 'POST':
        serializer = serializers.StudentSerializer(data = request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
        
    # return HttpResponse('data')

@api_view(['GET' , 'PATCH' , 'DELETE'])
def single_data(request , pk):

    try:
        student = Student.objects.get(pk= pk)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method  == 'GET':
        serializer = serializers.StudentSerializer(student)
        return Response(serializer.data  ,status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        serializer = serializers.StudentSerializer(student , data = request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)     

    if request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # serializer = serializers.StudentSerializer(student , data = request.data)
        # if serializer.is_valid():
        #     serializer.delete




#class based view :

class Teachers_data(APIView):
    def get(self , request):
        teacher = Teachers.objects.all()
        serializer = serializers.TeacherSerializer(teacher , many = True)

        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        teacher = Teachers.objects.all()
        serializer = serializers.TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    

class teacher_detail(APIView):
    def get_object(self , pk ):
        try:
            return Teachers.objects.get(pk = pk)
        
        except Teachers.DoesNotExist:
            raise Http404
        
    def get(self , request ,pk):
        teacher = self.get_object(pk=pk)
        serializer = serializers.TeacherSerializer(teacher)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def put(self , request , pk):
        teacher = self.get_object(pk=pk)
        serializer = serializers.TeacherSerializer(teacher , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request,pk):
        teacher = self.get_object(pk = pk)
        teacher.delete()
        return Response(  {"message": "Student deleted successfully"},status=status.HTTP_204_NO_CONTENT)
    

#mixins :

class user_data(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):

    queryset = user.objects.all()
    serializer_class = serializers.UserSerializer
    
    def get(self , request):
        return self.list(request)
   
    def post(self, request):
        return self.create(request)
    

class single_user(mixins.RetrieveModelMixin , mixins.DestroyModelMixin ,mixins.UpdateModelMixin , generics.GenericAPIView):

    queryset = user.objects.all()
    serializer_class = serializers.UserSerializer

    def get(self , request , pk):
        return self.retrieve(request , pk)
    
    def put(self , request ,pk):
        return self.update(request ,pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)