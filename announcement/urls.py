from django.urls import path
from . import views

urlpatterns = [
    path('',views.announcement,name='announcement'),
]