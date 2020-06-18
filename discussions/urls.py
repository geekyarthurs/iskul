from django.urls import path, include

from . import views

app_name = 'discussions'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('question/<int:pk>/', views.QuestionView.as_view(), name='question'),
    path('question/<int:pk>/answer/',
         views.AnswerView.as_view(),
         name='answer'),
    path('question/add/', views.AddQuestionView.as_view(), name = 'add_question')
]
