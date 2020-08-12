from django.urls import path
from . import views

urlpatterns = [
    path('external_contents/<str:slug>', views.contentDetails , name="content_details"),
    path('external_contents/', views.contents , name="contents"),
    
    
]
