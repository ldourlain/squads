from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Classroom
from .forms import AddClassForm


def classroom(request, classroom_id):
    current_classroom = get_object_or_404(Classroom, id=classroom_id)
    context = {"students": current_classroom.student_ids.all()}
    return render(request, 'classroom.html', context)


def classes(request):
    context = {"classes": Classroom.objects.all()}
    return render(request, 'classes.html', context)


def edit_groups(request, classroom_id, group_set):
    json = {"teams": [
        ["abc123", "lol34", "hah456", "ok99"],
        ["lcd64", "emf86", "tmh327", "sd3424"],
        ["sad32", "xd69", "pls420"]
    ],
        "absences": []
    }
    return render(request, 'edit_classes.html', {"json": json})

@csrf_exempt
@require_http_methods(["POST", "GET"])
def add_class(request):
    if request.method == "POST":
        form = AddClassForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.owner = request.user
            classroom.save()
        return redirect('classes')
    else:
        form = AddClassForm()
    return render(request, 'new-class.html', {'form': form})

#def add_class_student(request):
    #render to
# def generate_group(request, classroom_id, min_partners, pref_partners):
#     current_classroom = get_object_or_404(Classroom, id=classroom_id)
#     num = current_classroom.num_of_groups + 1
#     for i in range()
#
