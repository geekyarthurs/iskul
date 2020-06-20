from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid
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

    # slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.course_name + " " + str(self.class_name)

    def get_absolute_url(self):
        return reverse("classroom:dashboard")


class Chapter(models.Model):
    course_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    chapter_title = models.CharField(max_length=100)
    chapter_number = models.PositiveIntegerField()

    # slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.chapter_number) + ". " + self.chapter_title

    def get_absolute_url(self):
        return reverse("classroom:dashboard")


class Content(models.Model):

    topic = models.CharField(max_length=100)

    course_name = models.ForeignKey(Chapter, on_delete=models.CASCADE)

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


# def pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         slug = slugify(instance.chapter_title + str(uuid.uuid1()))
#         instance.slug = slug

# # pre_save.connect(pre_save_receiver, sender=Chapter)
# pre_save.connect(pre_save_receiver, sender=Subject)
