from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class MyUser(AbstractUser):

    gender = models.BooleanField(null=True, blank=True)
    mobile_number = models.CharField(max_length=10, unique=True, null=True)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username


class Student(models.Model):

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    roll_no = models.PositiveIntegerField()
    grades = models.PositiveIntegerField()  # class

    def __str__(self):
        return self.user.username


class Teacher(models.Model):

    SUBJECTS = (
        ("M", "MATH"),
        ("S", "SCIENCE"),
    )

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    subject = models.CharField(max_length=1, choices=SUBJECTS)

    def __str__(self):
        return self.user.username