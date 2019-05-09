from django.shortcuts import HttpResponse, render
from django.views.generic import View
from .models import StudentModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializers
from rest_framework import generics


class StudentView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers
