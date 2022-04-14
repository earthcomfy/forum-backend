from django.contrib import admin
from .models import Answer, QuestionCategory, Question, QuestionComment, AnswerComment


admin.site.register(QuestionCategory)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionComment)
admin.site.register(AnswerComment)
