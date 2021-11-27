from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.core.validators import RegexValidator

from .managers import StudentManager


class Student(AbstractBaseUser, PermissionsMixin):
    DEPARTMENTS = [
        ('fcfe', (
            ('CE', 'Chemical Engineering'),
            ('FE', 'Food Engineering'),
            ('AHN', 'Applied Human Nutrition')
        )),
        ('fcwre', (
            ('WRE', 'Water |Resoures Engineering'),
            ('CIE', 'Civil Engineering')
        )),
        ('fc', (
            ('SE', 'Software Engineering'),
            ('CS', 'Computer Science'),
            ('IT', 'Information Technology'),
            ('IS', 'Information Science'),
        )),
        ('fece', (
            ('COE', 'Computer Engineering'),
            ('EE', 'Electrical Engineering'),
        )),
        ('fmie', (
            ('ME', 'Mechanical Engineering'),
            ('IE', 'Industrial Engineering'),
            ('AE', 'Automotive Engineering'),
            ('EME', 'Electro-Mechanical Engineering')
        ))
    ]
    name = models.CharField(_('name'), max_length=100, validators=[
                            RegexValidator(r'^[a-zA-Z ]+$')])
    student_id = models.CharField(_('student id'), unique=True, max_length=7, validators=[
                                  RegexValidator(r'^\d{1,10}$')])
    email = models.EmailField(_('email address'), unique=True)
    dept_choice = models.CharField(max_length=3, choices=DEPARTMENTS)
    username = None
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = StudentManager()

    def get_full_name(self):
        return self.name
