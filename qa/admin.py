from django.contrib import admin
from .models import Answer, QuestionCategory, Question


admin.site.register(QuestionCategory)
admin.site.register(Question)
admin.site.register(Answer)
