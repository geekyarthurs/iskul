from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/student/',
         views.StudentRegister.as_view(),
         name='student_register'),
    path('register/teacher/',
         views.TeacherRegister.as_view(),
         name='teacher_register'),
]
