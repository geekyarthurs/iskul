from django.shortcuts import render
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.shortcuts import resolve_url
from .models import Grade, Content, Subject, Chapter


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, views.View):

    template_url = "classroom/subjects_page.html"

    def test_func(self):
        login_url = "accounts:login"
        return self.request.user.is_student

    def get(self, request):
        grade = request.user.student.grades
        className = grade.className

        subjects = grade.subject_set.all()

        context = {'grade': className, 'subjects': subjects}

        return render(request, self.template_url, context)


class ContentPage(LoginRequiredMixin, UserPassesTestMixin, views.View):
    template_url = "classroom/content_page.html"

    def test_func(self):
        login_url = "accounts:login"
        return self.request.user.is_student

    def get(self, request, subject, chapter=None):

        chapters = Subject.objects.get(pk=subject).chapter_set.all()

        print(chapters)

        if chapter == None:
            content = Chapter.objects.all().first().content_set.all()
        else:
            content = Chapter.objects.get(pk=chapter).content_set.all()

        context = {'chapters': chapters, 'contents': content}
        # content =

        return render(request, self.template_url, context)
