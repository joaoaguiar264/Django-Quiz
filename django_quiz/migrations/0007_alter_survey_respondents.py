# Generated by Django 4.2.7 on 2023-12-06 22:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_quiz', '0006_survey_respondents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='respondents',
            field=models.ManyToManyField(blank=True, default=[], related_name='surveys_responded', to=settings.AUTH_USER_MODEL),
        ),
    ]
