from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class QuestionCategory(models.Model):
    name = models.CharField(_('Category name'), max_length=100)

    class Meta:
        verbose_name = _('Question Category')
        verbose_name_plural = _('Question Categories')

    def __str__(self):
        return self.name


def get_default_question_category():
    """
    Returns a default question category.
    """
    return QuestionCategory.objects.get_or_create(name='Others')[0]


class Question(models.Model):
    title = models.CharField(_('Question title'), max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="questions", null=True, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(
        QuestionCategory, related_name="question_list")
    body = models.TextField(_('Question body'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="answers", null=True, on_delete=models.SET_NULL)
    question = models.ForeignKey(
        Question, related_name="answer", on_delete=models.CASCADE)
    body = models.TextField(_('Answer body'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.body


class BaseComment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="%(app_label)s_%(class)s_comments", null=True, on_delete=models.SET_NULL)
    body = models.TextField(_('Comment body'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at', )

    def __str__(self):
        return self.body


class QuestionComment(BaseComment):
    question = models.ForeignKey(
        Question, related_name="comment_list", on_delete=models.CASCADE)


class AnswerComment(BaseComment):
    answer = models.ForeignKey(
        Answer, related_name="answer_list", on_delete=models.CASCADE)
