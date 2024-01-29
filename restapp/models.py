from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    marks = models.FloatField()
    stream = models.CharField(max_length=100)

    def __str__(self):
        return self.name