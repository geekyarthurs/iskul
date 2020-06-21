from django.urls import path
from . import views


app_name = 'classroom'

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('subject/<int:subject>/chapter/<int:chapter>/',
         views.ContentPage.as_view(),
         name='content_page_yes'),
    path('subject/<int:subject>/chapter/<int:chapter>/page/<int:page>',
         views.ContentPage.as_view(),
         name='content_page_paged'),
    path('subject/<int:subject>/',
         views.ContentPage.as_view(),
         name='content_page_no'),
    path('chapter_create/',
         views.ChapterCreate.as_view(),
         name='chapter_create'),
    path('chapter_delete/<int:chapter_id>/',
         views.DeleteChapter.as_view(),
         name='chapter_delete'),
    path('content_create/course/<int:course_id>/chapter/<int:chapter_id>/',
         views.ContentCreate.as_view(),
         name='content_create'),
    path('manage_student/',
         views.StudentManage.as_view(),
         name='student_manage'),
    path('user_delete/<int:user_id>',
         views.DeleteUser.as_view(),
         name='user_delete'),
    path('toggle_user/<int:user_id>',
         views.ToggleActive.as_view(),
         name='user_toggle'),
    path('update_student/<int:pk>/',
         views.UpdateStudent.as_view(),
         name='update_student'),
    path('update_user/<int:pk>',
         views.UpdateUser.as_view(),
         name='update_user')
]
