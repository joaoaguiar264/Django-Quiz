# Generated by Django 4.2.8 on 2023-12-05 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_quiz', '0002_survey_is_open_survey_option1_survey_option1_results_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='option1_results',
            field=models.IntegerField(blank=True, max_length=255),
        ),
    ]