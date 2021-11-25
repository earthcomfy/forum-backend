from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Student


class StudentCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ('name', 'student_id', 'dept_choice', 'email',)


class StudentChangeForm(UserChangeForm):
    class Meta:
        model = Student
        fields = ('name', 'student_id', 'dept_choice', 'email',)
