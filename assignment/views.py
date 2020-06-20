from django.shortcuts import render
from django import views
from .models import Assignment, AssignmentSubmission
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from . import forms


class Home(LoginRequiredMixin, UserPassesTestMixin, views.View):
    def test_func(self):
        return True

    def get(self, request):
        if request.user.is_student:
            user_grade = request.user.student.grades
        else:
            user_grade = request.user.teacher.grade
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

        try:
            submission = AssignmentSubmission.objects.get(
                answered_by=request.user.student)
        except:
            submission = None

        form = forms.AddSubmission()
        context = {
            "assignment": assignment,
            "submission": submission,
            "form": form
        }

        return render(request, "assignment/student_assignment.html", context)

    def post(self, request, assignment_id):

        answered_by = request.user
        assignment = Assignment.objects.get(pk=assignment_id)

        form = forms.AddSubmission(request.POST)

        if form.is_valid():
            sub = form.save(commit=False)
            sub.answered_by = answered_by
            sub.assignment = assignment
            sub.save()

            return redirect(request,
                            'assignment:assignment_id',
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
    return redirect(request,
                    'assignment:assignment_id',
                    assignment_id=assignment_id)
