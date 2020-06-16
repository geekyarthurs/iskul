from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from django.shortcuts import reverse


# Create your models here.
class MyUser(AbstractUser):

    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
    )

    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    mobile_number = models.CharField(max_length=10, unique=True, null=True)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username

    @property
    def is_student(self):
        return hasattr(self, 'student')

    @property
    def is_teacher(self):
        return hasattr(self, 'teacher')


class Student(models.Model):

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    roll_no = models.PositiveIntegerField()
    grades = models.ForeignKey(to='classroom.Grade', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("classroom:student_manage")

    def __str__(self):
        return self.user.username


class Teacher(models.Model):

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    subject = models.ForeignKey(to='classroom.Subject',
                                on_delete=models.CASCADE)
    grades = models.ForeignKey(to='classroom.Grade', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
