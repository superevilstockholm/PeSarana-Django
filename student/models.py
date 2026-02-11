from django.db import models

from core.models import TimeStampModel

# Create your models here.
class Student(TimeStampModel):
    nisn = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    dob = models.DateField()
