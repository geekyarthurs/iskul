from django.db import models
from django.db.models.functions import datetime

# Create your models here.


class Assignment(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    question_file = models.FileField(upload_to="questions")
    submission_date = models.DateField()

    given_by = models.ForeignKey(to='accounts.Teacher',
                                 on_delete=models.CASCADE)
    given_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AssignmentSubmission(models.Model):

    assignment = models.ForeignKey(to=Assignment,
                                   related_name='submissions',
                                   on_delete=models.CASCADE)
    assignment_file = models.FileField(upload_to="answers")

    checked = models.BooleanField(null=True, default=False)
    received_grade = models.PositiveIntegerField(default=0, blank=True)
    answered_by = models.ForeignKey(to='accounts.Student',
                                    on_delete=models.CASCADE)
