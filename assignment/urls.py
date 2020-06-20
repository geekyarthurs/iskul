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
    ),
    path(
        'delete_submission/<int:submission_id>',
        views.delete_submission,
        name='delete_submission',
    )
]
