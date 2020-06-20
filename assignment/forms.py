from django import forms
from .models import AssignmentSubmission


class AddSubmission(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ('assignment_file', )
