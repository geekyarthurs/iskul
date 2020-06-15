from django import forms
from . import models


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        super().clean()

        p1 = self.cleaned_data.get("password")
        p2 = self.cleaned_data.get("confirm_password")

        if p1 != p2:
            forms.ValidationError("Error! Password Must Match!")
        else:
            return self.cleaned_data

        # self.cleaned_data

    class Meta:
        model = models.MyUser
        fields = ('username', 'password')


class TeacherCreationForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['subject']


class StudentCreationForm(forms.ModelForm):
    grades = forms.IntegerField(label="Class")

    class Meta:
        model = models.Student
        fields = ['grades', 'roll_no']
