from django.shortcuts import render
from django import views
from .models import Assignment, AssignmentSubmission
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


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
        context = {
            "assignment": assignment,
            "submission": submission,
        }

        return render(request, "assignment/student_assignment.html", context)
