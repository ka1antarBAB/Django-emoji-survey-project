# Generated by Django 5.1 on 2024-08-12 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_survey_surveygroup_delete_emojifeedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveygroup',
            name='survey',
        ),
        migrations.AddField(
            model_name='survey',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='surveys', to='survey.surveygroup'),
            preserve_default=False,
        ),
    ]