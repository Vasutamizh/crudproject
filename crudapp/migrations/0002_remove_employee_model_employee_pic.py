# Generated by Django 5.0.1 on 2024-02-01 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_model',
            name='Employee_pic',
        ),
    ]