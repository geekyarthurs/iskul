from django.shortcuts import render
from django import views
from . import forms
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


class Admit(views.View):

    template_name = "admission/admission_form.html"

    def get(self, request):
        AdmitForm = forms.AdmissionForm()  # BASE USER
        context = {'form': AdmitForm}

        return render(request, self.template_name, context)

    def post(self, request):

        AdmitForm = forms.AdmissionForm(request.POST)
    
        if AdmitForm.is_valid():
            new_student = AdmitForm.save()
            new_student.save()
            return HttpResponse("form ok")

        else:
            context = {'form': AdmitForm}
            return render(request, self.template_name, context)
