from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    course_name = models.CharField(max_length=50)
    experience = models.IntegerField()
    email = models.EmailField()