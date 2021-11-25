from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import StudentCreationForm, StudentChangeForm
from .models import Student


class CustomUserAdmin(UserAdmin):
    add_form = StudentCreationForm
    form = StudentChangeForm

    model = Student
    
    list_display = ('name', 'student_id', 'dept_choice', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('name', 'student_id', 'dept_choice', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'student_id', 'dept_choice', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Student, CustomUserAdmin)
