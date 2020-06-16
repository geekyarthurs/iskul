from django.urls import path
from . import views
from classroom import views as cl_view
app_name = 'accounts'

urlpatterns = [
    path('register/student/',
         views.StudentRegister.as_view(),
         name='student_register'),
    path('register/teacher/',
         views.TeacherRegister.as_view(),
         name='teacher_register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.signout, name='signout'),
    path('', cl_view.Dashboard.as_view(), name='dash')
]
