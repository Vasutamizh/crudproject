# Generated by Django 5.0.1 on 2024-02-01 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_remove_employee_model_employee_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_model',
            name='Employee_joining_date',
            field=models.DateField(auto_now=True),
        ),
    ]
