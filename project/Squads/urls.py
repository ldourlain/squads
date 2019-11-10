from django.urls import path
from . import views

urlpatterns = [
    path('classroom/<int:classroom_id>/', views.classroom, name='classroom'),
    path('classes/', views.classes, name='classes'),
    path('generate/<int:classroom_id>/<int:num_partners>', views.generate_groups, name='generate_groups'),
    path('edit-groups/<int:classroom_id>/<int:group_set>', views.edit_groups, name='edit_groups'),
    path('upload-json/<int:classroom_id>', views.save_group, name='save_group'),
    path('upload-json/<int:classroom_id>/<int:group_set>', views.save_group, name='save_group')
]
