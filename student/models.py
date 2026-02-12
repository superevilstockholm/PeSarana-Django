from django.db import models

# Models
from core.models import TimeStampModel
from classroom.models import Classroom
from user.models import User

# Create your models here.
class Student(TimeStampModel):
    nisn = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)