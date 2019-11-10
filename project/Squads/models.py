from django.db import models
from Users.models import Administrator


# Create your models here.

class Student(models.Model):
    full_name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)


class Classroom(models.Model):
    owner = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    student_ids = models.ManyToManyField(Student)
    num_of_groups = models.IntegerField()


class Group(models.Model):
    student_ids = models.ManyToManyField(Student)
    classroom_id = models.ForeignKey('Classroom', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    group_set = models.IntegerField()


class Absence(models.Model):
    student_ids = models.ManyToManyField(Student)
    classroom_id = models.ForeignKey('Classroom', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
