from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Classroom, Group, Student, Absence
import random
import json
from .forms import AddClassForm, AddClassStudent, AddStudent


def dashboard(request):
    return render(request, 'dashboard.html')


def classroom(request, classroom_id):
    current_classroom = get_object_or_404(Classroom, id=classroom_id)
    context = {"students": current_classroom.student_ids.all(), "classroom_id": classroom_id, "name": current_classroom.name}
    return render(request, 'classroom.html', context)


def classes(request):
    context = {"classes": Classroom.objects.all()}
    return render(request, 'classes.html', context)


def students(request):
    context = {"students": Student.objects.all()}
    return render(request, 'students.html', context)


def edit_groups(request, classroom_id, group_set):
    current_classroom = get_object_or_404(Classroom, id=classroom_id)

    groups = Group.objects.filter(group_set=group_set, classroom_id=current_classroom)

    final_groups = []
    for i in groups:
        members = []
        for j in i.student_ids.all():
            members.append(j.email)
        final_groups.append(members)

    absences = Absence.objects.filter(group_set=group_set, classroom_id=current_classroom)
    final_absences = []
    for i in absences:
        people = []
        for j in i.student_ids.all():
            people.append(j.email)
        final_absences.append(people)

    json = {"teams": final_groups,
            "absences": final_absences
            }
    current_classroom = get_object_or_404(Classroom, id=classroom_id)
    return render(request, 'edit_classes.html', {"json": json, "group_set": group_set, "classroom_id": classroom_id})


def generate_groups(request, classroom_id, num_partners):
    current_classroom = get_object_or_404(Classroom, id=classroom_id)
    past_groups_objects = current_classroom.group_set.all()
    past_groups = []
    for i in past_groups_objects:
        temp = []
        for j in i.student_ids.all():
            temp.append(j.email)
        past_groups.append(temp)

    students = current_classroom.student_ids.all()
    master_list = []
    teams = "{"
    partners_arr = str([""] * len(students))
    for i, student in enumerate(students):
        master_list.append(student.email)
        teams += "'" + student.email + "' : {" \
                                       "'name':'" + student.full_name + "','index':" + str(
            i) + ",'partners':" + partners_arr + "},"
    teams += "}"
    return render(request, 'generate_classes.html', {"num_partners": num_partners, "past_groups": str(past_groups),
                                                     "classroom_id": classroom_id, "teams": teams,
                                                     "master_list": str(master_list)})


def save_group(request, classroom_id, group_set=None):
    if request.method != "POST":
        return Http404()

    received_json_data = json.loads(request.body)

    current_classroom = get_object_or_404(Classroom, id=classroom_id)

    if group_set is None:
        current_classroom.num_of_groups += 1
        current_classroom.save()
        group_set = current_classroom.num_of_groups

    else:
        groups = Group.objects.filter(group_set=group_set, classroom_id=classroom_id)
        for i in groups:
            i.delete()

        absences = Absence.objects.filter(group_set=group_set, classroom_id=classroom_id)
        for i in absences:
            i.delete()

    for i in received_json_data['teams']:
        group = Group(group_set=group_set, classroom_id=current_classroom)
        group.save()
        for j in i:
            try:
                group.student_ids.add(Student.objects.get(email=j))
            except:
                pass
        group.save()

    absence = Absence(group_set=group_set, classroom_id=current_classroom)
    absence.save()
    for i in received_json_data['absences']:
        try:
            absence.student_ids.add(Student.objects.get(email=i))
        except:
            pass
    absence.save()

    return HttpResponse("/edit-groups/" + str(classroom_id) + "/" + str(group_set))


@require_http_methods(["POST", "GET"])
def add_students(request):
    if request.method == "POST":
        form = AddStudent(request.POST)
        if form.is_valid():
            student = form.save()
        return redirect('students')
    else:
        form = AddStudent()
    return render(request, 'new_students.html', {'form': form})


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


@require_http_methods(["POST", "GET"])
def add_class_student(request, classroom_id):
    current_classroom = get_object_or_404(Classroom, id=classroom_id)
    if request.method == "POST":
        form = AddClassStudent(request.POST, instance=current_classroom)
        if form.is_valid():
            current_classroom = form.save()
        return redirect('classroom', classroom_id=classroom_id)
    else:
        form = AddClassStudent(instance=current_classroom)
    return render(request, 'add_class_students.html', {'form': form})
