from rest_framework import serializers
from .models import StudentModel


class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = StudentModel
        fields = '__all__'
