from .models import StudentModel
from .serializers import StudentSerializers
from rest_framework import generics


class StudentView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers
