from django.shortcuts import render
from django import views
from .models import Assignment, AssignmentSubmission
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from . import forms
from django.http import HttpResponse
from django.db.models import Count
from accounts.models import Student


class TeacherHome(LoginRequiredMixin, UserPassesTestMixin, views.View):
    def test_func(self):
        return self.request.user.is_teacher

    def get(self, request):
        teacher_grade = request.user.teacher.grades
        assignments = Assignment.objects.filter(
            given_by__grades=teacher_grade).prefetch_related(
                'given_by').order_by('given_at').annotate(
                    total_submission=Count('submissions'))

        student_count = Student.objects.filter(grades=teacher_grade).count()

        context = {
            "assignments": assignments,
            "student_count": student_count,
        }

        return render(request, "assignment/teacher_index.html", context)


class Home(LoginRequiredMixin, UserPassesTestMixin, views.View):
    def test_func(self):
        return True

    def get(self, request):
        if request.user.is_student:
            user_grade = request.user.student.grades
        else:
            return redirect('assignment:teacher_home')
        assignments = Assignment.objects.filter(
            given_by__grades=user_grade).prefetch_related('given_by').order_by(
                'given_at')
        return render(request, "assignment/index.html",
                      {"assignments": assignments})


class AssignmentViewStudent(LoginRequiredMixin, UserPassesTestMixin,
                            views.View):
    def test_func(self):
        return self.request.user.is_student

    def get(self, request, assignment_id):

        assignment = Assignment.objects.get(pk=assignment_id)

        print(assignment.title)

        try:
            submission = AssignmentSubmission.objects.get(
                answered_by=request.user.student)
        except:
            submission = None

        form = forms.AddSubmission()
        context = {
            "assignments": assignment,
            "submission": submission,
            "form": form
        }

        return render(request,
                      "assignment/student_assignment.html",
                      context=context)

    def post(self, request, assignment_id):

        answered_by = request.user.student
        assignment = Assignment.objects.get(pk=assignment_id)

        form = forms.AddSubmission(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            sub = form.save(commit=False)
            sub.answered_by = answered_by
            sub.assignment = assignment
            sub.save()

            return redirect('assignment:student_assignment',
                            assignment_id=assignment_id)
        context = {
            "assignment": assignment,
            "submission": None,
            "form": form,
        }
        print(form.errors)
        return render(request, "assignment/student_assignment.html", context)


@login_required
def delete_submission(request, submission_id):

    instance = AssignmentSubmission.objects.get(pk=submission_id)
    assignment_id = instance.assignment_id
    instance.assignment_file.delete()
    instance.delete()
    return redirect('assignment:student_assignment',
                    assignment_id=assignment_id)


@login_required
def delete_assignment(request, assignment_id):
    instance = Assignment.objects.get(pk=assignment_id)
    instance.question_file.delete()
    instance.delete()
    return redirect('assignment:home')


class CreateAssignmentView(LoginRequiredMixin, UserPassesTestMixin,
                           views.View):

    template_name = "assignment/create_assignment.html"

    def test_func(self):
        return self.request.user.is_teacher

    def get(self, request):
        create_assignment_form = forms.CreateAssignment()

        context = {"form": create_assignment_form}

        return render(request, self.template_name, context)

    def post(self, request):

        create_assignment_form = forms.CreateAssignment(
            request.POST, request.FILES)

        if create_assignment_form.is_valid():
            assignment = create_assignment_form.save(commit=False)
            assignment.given_by = request.user.teacher
            assignment.save()

            return redirect('assignment:home')
        else:
            return render(request, self.template_name,
                          {"form": create_assignment_form})


class UpdateAssignmentView(LoginRequiredMixin, UserPassesTestMixin,
                           views.View):

    template_name = "assignment/update_assignment.html"

    def test_func(self):
        return self.request.user.is_teacher

    def get(self, request, assignment_id):
        assignment = Assignment.objects.get(pk=assignment_id)
        create_assignment_form = forms.UpdateAssignment(instance=assignment)

        context = {"form": create_assignment_form}

        return render(request, self.template_name, context)

    def post(self, request, assignment_id):

        create_assignment_form = forms.UpdateAssignment(request.POST, request.FILES)

        if create_assignment_form.is_valid():
            assignment = create_assignment_form.save(commit=False)
            assignment.given_by = request.user.teacher
            assignment.save()

            return redirect('assignment:home')
        else:
            return render(request, self.template_name,
                          {"form": create_assignment_form})
