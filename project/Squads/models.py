from django.db import models

# Create your models here.

class Student(models.Model):
    full_name = models.CharField(80)

class Classroom(models.Model):
    teacher_name = models.CharField(80)
    student_ids = models.ManyToManyField(Student)
    
class Group(models.Model):
    student_ids = models.ManyToManyField(Student)
    classroom_id = models.ForeignKey('Classroom',on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

class Absence(models.Model):
    student_ids = models.ManyToManyField(Student)
    classroom_id = models.ForeignKey('Classroom',on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)