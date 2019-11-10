from django import forms
from .models import Classroom, Student


class AddClassForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ('name',)


class AddClassStudent(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ('student_ids',)
