from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework_simplejwt import token_blacklist

from .forms import UserCreationForm, UserChangeForm
from .models import User, Student


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    model = User

    list_display = ('name', 'email', 'role',
                    'is_active', 'is_staff', 'is_superuser', 'last_login',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'role', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'role', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.register(User, UserAdmin)
admin.site.register(Student)

admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken,
                    OutstandingTokenAdmin)
