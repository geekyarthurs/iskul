from django.db import models
from django.contrib.auth import get_user_model

from classroom.models import Subject

User = get_user_model()


# Create your models here.
class Question(models.Model):

    question_title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question_content = models.TextField()
    # answered = models.BooleanField(default=False, blank=True)
    posted_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_title


class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer

    def get_absolute_url(self):
        return reverse("discussions:question", kwargs={"pk": self.question.pk})
