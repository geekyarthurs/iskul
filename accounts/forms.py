from django import forms
from . import models
from admission.models import Admission


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
        fields = ('first_name', 'last_name', 'username', 'password', 'gender',
                  'mobile_number', 'location')


class TeacherCreationForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ['subject', 'grades']


class StudentCreationForm(forms.ModelForm):
    # grades = forms.IntegerField(label="Class")

    promo_code = forms.CharField()

    class Meta:
        model = models.Student
        fields = ['grades', 'roll_no']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        super().clean()

        promo = self.cleaned_data['promo_code']
        user = Admission.objects.get(promo_code=promo)

        if not user.exists():
            raise forms.ValidationError("Wrong Promo Code.")
        else:
            user = Admission.objects.filter(promo_code=promo)
            user.registered_user = True
            return self.cleaned_data
