from django.test import TestCase
from . models import StudentModel
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .serializers import *


class ModelTestCase(TestCase):

    def create_object(self, first_name='Anthony', last_name='Pratt', age=4):
        return StudentModel.objects.create(first_name=first_name, last_name=last_name, age=age)

    def test_object_exist(self):
        w = self.create_object()
        self.assertTrue(isinstance(w, StudentModel))
