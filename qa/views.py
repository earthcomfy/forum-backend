from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Question, Answer, QuestionComment, AnswerComment
from .permissions import IsUserAuthor
from .serializers import QuestionSerializer, AnswerModelSerializer, QuestionCommentSerializer, AnswerCommentSerializer


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


class AnswerListAPIView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerModelSerializer


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerModelSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class AnswerAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerModelSerializer
    permission_classes = (IsUserAuthor,)


class QuestionCommentListAPIView(generics.ListAPIView):
    queryset = QuestionComment.objects.all()
    serializer_class = QuestionCommentSerializer


class QuestionCommentCreateAPIView(generics.CreateAPIView):
    queryset = QuestionComment.objects.all()
    serializer_class = QuestionCommentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class QuestionCommentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionComment.objects.all()
    serializer_class = QuestionCommentSerializer
    permission_classes = (IsUserAuthor,)


class AnswerCommentListAPIView(generics.ListAPIView):
    queryset = AnswerComment.objects.all()
    serializer_class = AnswerCommentSerializer


class AnswerCommentCreateAPIView(generics.CreateAPIView):
    queryset = AnswerComment.objects.all()
    serializer_class = AnswerCommentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class AnswerCommentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswerComment.objects.all()
    serializer_class = AnswerCommentSerializer
    permission_classes = (IsUserAuthor,)
