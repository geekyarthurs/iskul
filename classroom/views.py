from django.shortcuts import render
from django import views
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.shortcuts import resolve_url, redirect
from .models import Grade, Content, Subject, Chapter


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, views.View):

    template_url = "classroom/subjects_page.html"

    def test_func(self):
        login_url = "accounts:login"
        return (self.request.user.is_student or self.request.user.is_teacher)

    def get(self, request):
        if request.user.is_student:
            grade = request.user.student.grades
        else:
            grade = request.user.teacher.grades
        className = grade.className

        subjects = grade.subject_set.all()

        context = {'grade': className, 'subjects': subjects}

        return render(request, self.template_url, context)


class ContentPage(LoginRequiredMixin, UserPassesTestMixin, views.View):
    template_url = "classroom/content_page.html"

    def test_func(self):
        login_url = "accounts:login"
        return (self.request.user.is_student or self.request.user.is_teacher)

    def get(self, request, subject, chapter=None):

        chapters = Subject.objects.get(
            pk=subject).chapter_set.order_by('chapter_number')

        print(chapters)

        if chapter == None:
            content = []
            chapter_name = ""
        else:
            content = Chapter.objects.get(pk=chapter).content_set.all()
            chapter_name = Chapter.objects.get(pk=chapter).chapter_title

        context = {
            'chapters': chapters,
            'contents': content,
            'subject_id': subject,
            'chapter_id': chapter,
            'chapter_name': chapter_name
        }
        # content =

        return render(request, self.template_url, context)


class ChapterCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self):
        login_url = "accounts:login"
        return (self.request.user.is_teacher)

    model = Chapter
    fields = '__all__'


class DeleteChapter(LoginRequiredMixin, UserPassesTestMixin, views.View):
    def test_func(self):
        login_url = "accounts:login"
        return (self.request.user.is_teacher)

    def get(self, request, chapter_id):
        Chapter.objects.get(pk=chapter_id).delete()
        return redirect('classroom:dashboard')


class ContentCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self):
        login_url = "accounts:login"
        return (self.request.user.is_teacher)

    model = Content
    fields = '__all__'

