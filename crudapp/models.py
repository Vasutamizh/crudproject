from django.db import models

class Employee_Model(models.Model):
    Employee_Name = models.CharField(max_length=50)
    Employee_Age = models.IntegerField()
    Employee_joining_date = models.CharField(max_length=50, null=False)
    Last_modified = models.DateField(auto_now=True)




