from django.contrib import admin
from .models import QuestionCategory, Question


admin.site.register(QuestionCategory)
admin.site.register(Question)
