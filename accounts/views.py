from django.shortcuts import render
from django import views
from . import forms
from django.http import HttpResponse


class StudentRegister(views.View):

    template_name = "accounts/StudentSignup.html"

    def get(self, request):
        BaseForm = forms.UserCreationForm()  # BASE USER
        StudentForm = forms.StudentCreationForm()  # Student Creation Form

        context = {'base': BaseForm, 'student_form': StudentForm}

        return render(request, self.template_name, context)

    def post(self, request):

        baseForm = forms.UserCreationForm(request.POST)
        studentForm = forms.StudentCreationForm(request.POST)

        if baseForm.is_valid() and studentForm.is_valid():
            user = baseForm.save()
            user.set_password(user.password)
            user.save()
            student = studentForm.save(commit=False)
            student.user = user
            student.save()
            return HttpResponse("form ok")

        else:
            context = {'base': baseForm, 'student_form': studentForm}
            return render(request, self.template_name, context)


class TeacherRegister(views.View):

    template_name = "accounts/TeacherSignup.html"

    def get(self, request):
        BaseForm = forms.UserCreationForm()  # BASE USER
        TeacherForm = forms.TeacherCreationForm()  # Student Creation Form

        context = {'base': BaseForm, 'teacher_form': TeacherForm}

        return render(request, self.template_name, context)

    def post(self, request):

        baseForm = forms.UserCreationForm(request.POST)
        teacherForm = forms.TeacherCreationForm(request.POST)

        if baseForm.is_valid() and teacherForm.is_valid():
            user = baseForm.save()
            user.set_password(user.password)
            user.save()
            teacher = teacherForm.save(commit=False)
            teacher.user = user
            teacher.save()
            return HttpResponse("form ok")

        else:
            context = {'base': baseForm, 'student_form': teacherForm}
            return render(request, self.template_name, context)
