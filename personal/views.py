from django.shortcuts import render
from rest_framework import viewsets
from .models import Personnel, Department
from .serializers import PersonnelSerializer, DepartmentSerializer

class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PersonnelView(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    