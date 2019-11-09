from django.db import models
from Users.models import Administrator

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=80)

class Classroom(models.Model):
    name = models.CharField(max_length=80)
    teacher_name = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    student_ids = models.ManyToManyField(Student)

class Group(models.Model):
    student_ids = models.ManyToManyField(Student)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

class Absence(models.Model):
    student_ids = models.ManyToManyField(Student)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)