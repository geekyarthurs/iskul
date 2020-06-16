from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('subject/<int:subject>/chapter/<int:chapter>/',
         views.ContentPage.as_view(),
         name='content_page_yes'),
    path('subject/<int:subject>/',
         views.ContentPage.as_view(),
         name='content_page_no'),
    path('chapter_create/',
         views.ChapterCreate.as_view(),
         name='chapter_create'),
    path('chapter_delete/<int:chapter_id>/',
         views.DeleteChapter.as_view(),
         name='chapter_delete'),
    path('content_create/',
         views.ContentCreate.as_view(),
         name='content_create')
]
