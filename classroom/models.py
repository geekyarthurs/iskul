from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
User = get_user_model()


# Create your models here.
class Grade(models.Model):
    className = models.PositiveIntegerField()

    def __str__(self):
        return str(self.className)


class Subject(models.Model):
    class_name = models.ForeignKey(Grade, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=10)
    course_desc = models.TextField()

    def __str__(self):
        return self.course_name + " " + str(self.class_name)

    def get_absolute_url(self):
        return reverse("classroom:dashboard")


class Chapter(models.Model):
    course_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter_title = models.CharField(max_length=100)
    chapter_number = models.PositiveIntegerField()

    def __str__(self):
        return str(self.chapter_number) + ". " + self.chapter_title

    def get_absolute_url(self):
        return reverse("classroom:dashboard")


class Content(models.Model):

    CONTENT_TYPE = (
        ("1", "paragraph"),
        ("2", "video"),
        ("3", "image"),
    )

    topic = models.CharField(max_length=100)

    course_name = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    content = models.CharField(max_length=2, choices=CONTENT_TYPE)
    content_image = models.ImageField(upload_to="images",
                                      blank=True,
                                      null=True)
    content_video = models.FileField(upload_to='videos', blank=True, null=True)
    content_paragraph = models.TextField(blank=True, null=True)
    uploaded_at = models.DateField(auto_now=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.topic)

    def get_absolute_url(self):
        return reverse("classroom:dashboard")
