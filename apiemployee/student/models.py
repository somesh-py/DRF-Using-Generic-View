from django.db import models

# Create your models here.


class Student(models.Model):
    Student_Reg_Number=models.TextField(unique=True)
    Student_Name=models.TextField()
    Student_Email=models.TextField()
    Student_Mobile=models.TextField()
    Created_At=models.DateTimeField(auto_now=True)
    