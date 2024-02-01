from django.contrib import admin

# Register your models here.
from .models import Employee_Model
# Register your models here.

class Employee_Admin(admin.ModelAdmin):
    emp_details = ["Emp_Name", "Emp_age"]



admin.site.register(Employee_Model, Employee_Admin)