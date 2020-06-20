from django import forms
from . import models


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = models.Admission
        fields = (
            'student_name',
            'class_name',
            'guardian_name',
            'student_age',
            'student_dob',
            'student_address',
            'student_contact',
            'student_gender',
            'student_email',
            'student_photo',
        )
