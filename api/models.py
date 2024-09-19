from django.db import models

# Create your models here.

class Courses(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    seats = models.PositiveIntegerField()
    fee = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image',null=True)

    def __str__(self) :
        return self.title
    

class Student(models.Model):
     name=models.CharField(max_length=100)
     age=models.PositiveIntegerField()
     email=models.EmailField()
     qualification=models.CharField(max_length=100)
     course=models.ForeignKey(Courses,on_delete=models.CASCADE)

