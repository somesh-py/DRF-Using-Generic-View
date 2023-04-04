from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee
# Create your views here.


class EmployeeCreateApi(generics.CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeApi(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer