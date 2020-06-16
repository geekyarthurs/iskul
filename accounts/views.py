from django.shortcuts import render
from django import views
from . import forms
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect


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
            # user.is_active = False
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
            # user.is_active = False
            user.save()
            teacher = teacherForm.save(commit=False)
            teacher.user = user
            teacher.save()
            return HttpResponse("form ok")

        else:
            context = {'base': baseForm, 'student_form': teacherForm}
            return render(request, self.template_name, context)


class LoginView(views.View):

    template_name = "accounts/login.html"

    def get(self, request):
        loginForm = forms.LoginForm()

        context = {'form': loginForm}

        return render(request, self.template_name, context)

    def post(self, request):
        loginForm = forms.LoginForm(request.POST)

        if loginForm.is_valid():

            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            print(username)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                print(" user found")
                login(request, user)
                return redirect('classroom:dashboard')
            else:
                # loginForm.add_error(password, "Invalid Username or password")
                print("invalid username or password")
                context = {'form': loginForm}
        return render(request, self.template_name, context)


def signout(request):
    logout(request)
    return redirect('accounts:login')
