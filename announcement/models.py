from django.db import models
from classroom.models import Grade

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length= 50)
    content = models.TextField()
    date_announced = models.DateTimeField(auto_now=True)
    an_type = (
        ('Custom', 'Custom'),
        ('Public', 'Public'),
    )
    announcement_type = models.CharField(max_length=10, choices=an_type)
    class_name = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True, default="1")

    def __str__(self):
        return str(self.title)
