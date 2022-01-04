from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Question
from .permissions import IsUserAuthor
from .serializers import QuestionSerializer


class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class QuestionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsUserAuthor,)
