# Generated by Django 5.1 on 2024-08-11 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='balance',
        ),
    ]
