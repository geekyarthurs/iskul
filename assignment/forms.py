from django import forms
from .models import AssignmentSubmission, Assignment


class AddSubmission(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ('assignment_file', )


class CreateAssignment(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'question_file', 'submission_date']


class UpdateAssignment(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'question_file', 'submission_date']


class CheckAssignment(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ('received_grade', )
