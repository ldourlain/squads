from django.urls import path
from . import views

urlpatterns = [
    path('classroom/<int:classroom_id>/', views.classroom, name='classroom'),
    path('new-class/', views.add_class, name='add_class'),
    path('add_class_students/<int:classroom_id>/', views.add_class_student, name='add_class_student'),
    path('classes/', views.classes, name='classes'),
    path('edit-groups/<int:classroom_id>/<int:group_set>', views.edit_groups, name='edit_groups'),

]
