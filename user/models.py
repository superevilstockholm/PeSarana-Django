from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        STUDENT = 'STUDENT', 'Student'
    
    role = models.CharField(max_length=10, choices=Roles.choices, default=Roles.STUDENT)

    def is_admin(self) -> bool:
        return self.role == self.Roles.ADMIN

    def is_student(self) -> bool:
        return self.role == self.Roles.STUDENT