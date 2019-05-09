from django.db import models


class StudentModel(models.Model):
    first_name = models.CharField(max_length=44, null=False)
    last_name = models.CharField(max_length=44, null=False)
    age = models.IntegerField(null=False)
    title = models.CharField(max_length=22, default='Student')
    objects = models.Manager()

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)
