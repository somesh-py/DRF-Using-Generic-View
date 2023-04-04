from django.db import models

# Create your models here.

class Employee(models.Model):
    Emp_Regno=models.TextField(unique=True)
    Emp_Name=models.TextField()
    Emp_Email=models.TextField()
    Emp_Mobile=models.TextField(null=True)
    Created_At=models.DateTimeField(auto_now=True)