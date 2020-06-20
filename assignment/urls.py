from django.urls import path
from . import views

app_name = 'assignment'

urlpatterns = [
    path(
        '',
        views.Home.as_view(),
        name='home',
    ),
    path(
        'student/<int:assignment_id>',
        views.AssignmentViewStudent.as_view(),
        name='student_assignment',
    )
]
