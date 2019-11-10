from django.urls import path
from . import views

urlpatterns = [
    path('classroom/<int:classroom_id>/', views.classroom, name='classroom'),
    path('classes/', views.classes, name='classes'),
    path('edit-groups/<int:classroom_id>/<int:group_set>', views.edit_groups, name='edit_groups'),
]
