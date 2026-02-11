from django.db import models

# Models
from core.models import TimeStampModel

# Create your models here.
class Classroom(TimeStampModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()