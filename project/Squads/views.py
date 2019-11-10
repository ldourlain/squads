from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Classroom


def classroom(request, classroom_id):
    current_classroom = get_object_or_404(Classroom, id=classroom_id)
    context = {"students": current_classroom.student_ids.all()}
    return render(request, 'classroom.html', context)


def classes(request):
    context = {"classes": Classroom.objects.all()}
    return render(request, 'classes.html', context)
# Create your views here.
