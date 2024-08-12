# Generated by Django 5.1 on 2024-08-12 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji', models.CharField(choices=[('Happy', '😃'), ('Neutral', '😐'), ('Sad', '😞'), ('Love', '😍'), ('Angry', '😡')], max_length=10)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='survey.survey')),
            ],
        ),
        migrations.DeleteModel(
            name='EmojiFeedback',
        ),
    ]