from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


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
        User, related_name="questions", null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        QuestionCategory, related_name="question_list", on_delete=models.SET(get_default_question_category))
    body = models.TextField(_('Question body'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title
