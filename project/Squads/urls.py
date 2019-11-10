from django.urls import path
from . import views

urlpatterns = [
    path('classroom/<int:classroom_id>/', views.classroom, name='classroom'),
    path('new_class/', views.add_class, name='add_class'),
    path('add_class_students/<int:classroom_id>/', views.add_class_student, name='add_class_student'),
    path('classes/', views.classes, name='classes'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.students, name='students'),
    path('new_students/', views.add_students, name='add_students'),
    path('generate/<int:classroom_id>/<int:num_partners>', views.generate_groups, name='generate_groups'),
    path('edit-groups/<int:classroom_id>/<int:group_set>', views.edit_groups, name='edit_groups'),
    path('upload-json/<int:classroom_id>', views.save_group, name='save_group'),
    path('upload-json/<int:classroom_id>/<int:group_set>', views.save_group, name='save_group')
]
