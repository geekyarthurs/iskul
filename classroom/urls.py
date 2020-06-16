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
]
