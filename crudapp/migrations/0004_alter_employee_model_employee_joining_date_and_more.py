# Generated by Django 5.0.1 on 2024-02-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_alter_employee_model_employee_joining_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_model',
            name='Employee_joining_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee_model',
            name='Last_modified',
            field=models.DateField(auto_now=True),
        ),
    ]
