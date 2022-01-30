from django.urls import path
from . import views

app_name = 'qa'

urlpatterns = [
    path('question/create/', views.QuestionCreateAPIView.as_view(),
         name='create-question'),
    path('question/list/', views.QuestionListAPIView.as_view(),
         name='question-list'),
    path('question/<int:pk>/', views.QuestionAPIView.as_view(),
         name='question-detail'),

    path('answer/create/', views.AnswerCreateAPIView.as_view(),
         name='create-answer'),
    path('answer/list/', views.AnswerListAPIView.as_view(),
         name='answer-list'),
    path('answer/<int:pk>/', views.AnswerAPIView.as_view(),
         name='answer-detail'),

]
