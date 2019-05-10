from django.db import models


class StudentModel(models.Model):
    first_name = models.CharField(max_length=44, null=True)
    last_name = models.CharField(max_length=44, null=True)
    age = models.IntegerField(null=True)
    objects = models.Manager()

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)
