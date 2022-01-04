# Generated by Django 3.2.9 on 2021-12-31 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import qa.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=models.SET(qa.models.get_default_question_category), related_name='question_list', to='qa.questioncategory'),
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='qa.question'),
        ),
    ]
