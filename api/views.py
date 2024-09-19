from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from api.models import Courses,Student
from api.serializer import CourseModelSerializer,StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status




class CourseViewsetView(ModelViewSet):
    serializer_class=CourseModelSerializer

    queryset=Courses.objects.all()
    @action(methods=['POST'],detail=True)
    def add_student(self,request,*agrs,**kw):
        cid=kw.get('pk')
        course=self.queryset.get(id=cid)
        ser=StudentSerializer(data=request.data)
        if ser.is_valid():
            name=ser.validated_data.get('name')
            ag=ser.validated_data.get('age')
            em=ser.validated_data.get('email')
            qua=ser.validated_data.get('qualification')
            Student.objects.create(name=name,age=ag,email=em,qualification=qua,course=course)
            return Response(data=ser.data,status=status.HTTP_200_OK)
        return Response(data=ser.errors,status=status.HTTP_400_BAD_REQUEST)
    

    @action(methods=['GET'],detail=True)
    def get_student(self,request,*agrs,**kw):
        cid=kw.get('pk')
        course=self.queryset.get(id=cid)
        students=Student.objects.filter(course=course)
        ser=StudentSerializer(students,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)
    

