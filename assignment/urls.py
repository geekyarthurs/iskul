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
    ),
    path(
        'teacher/home',
        views.TeacherHome.as_view(),
        name='teacher_home',
    ),
    path(
        'teacher/create',
        views.CreateAssignmentView.as_view(),
        name='create_assignment',
    ),
    path(
        'teacher/delete/<int:assignment_id>',
        views.delete_assignment,
        name='delete_assignment',
    ),
    path(
        'teacher/update/<int:assignment_id>',
        views.UpdateAssignmentView.as_view(),
        name='update_assignment',
    )
]
