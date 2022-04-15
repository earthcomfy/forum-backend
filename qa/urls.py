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

    path('question/comment/create/', views.QuestionCommentCreateAPIView.as_view(),
         name='create-question-comment'),
    path('question/comment/list/', views.QuestionCommentListAPIView.as_view(),
         name='question-comment-list'),
    path('question/comment/<int:pk>/', views.QuestionCommentAPIView.as_view(),
         name='question-comment-detail'),

    path('answer/comment/create/', views.AnswerCommentCreateAPIView.as_view(),
         name='create-answer-comment'),
    path('answer/comment/list/', views.AnswerCommentListAPIView.as_view(),
         name='answer-comment-list'),
    path('answer/comment/<int:pk>/', views.AnswerCommentAPIView.as_view(),
         name='answer-comment-detail'),
]
