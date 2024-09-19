
from rest_framework import serializers
from api.models import Courses,Student


class CourseModelSerializer(serializers.ModelSerializer):

    class Meta:    #class about class 

        model=Courses
        fields="__all__"


class StudentSerializer(serializers.ModelSerializer):

    course=serializers.CharField(read_only=True)
    class Meta:    

        model=Student
        fields="__all__"