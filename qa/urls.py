from django.urls import path
from qa import views

app_name = 'question'

urlpatterns = [
    path('create/', views.QuestionCreateAPIView.as_view(),
         name='create-question'),
    path('list/', views.QuestionListAPIView.as_view(),
         name='question-list'),
    path('<int:pk>/', views.QuestionAPIView.as_view(),
         name='question-detail'),
]
