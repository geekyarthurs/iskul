from django.shortcuts import render
from django import views
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.shortcuts import resolve_url, redirect
from .models import Grade, Content, Subject, Chapter
from django.contrib.auth import get_user_model
from accounts.models import Student

from django.core.paginator import Paginator
from .forms import ContentCreateForm


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

    def get(self, request, subject, chapter=None, page=1):

        chapters = Subject.objects.get(
            pk=subject).chapter_set.order_by('chapter_number')

        # print(chapters)

        if chapter == None:
            content = []
            chapter_name = ""
        else:
            content = Chapter.objects.get(pk=chapter).content_set.all()

            chapter_name = Chapter.objects.get(pk=chapter).chapter_title

        p = Paginator(content, 5).page(page)

        content = p.object_list

        context = {
            'page': p,
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
    fields = ('chapter_title', 'course_name', 'chapter_number')


class DeleteChapter(LoginRequiredMixin, UserPassesTestMixin, views.View):
    def test_func(self):
        login_url = "accounts:login"
        return (self.request.user.is_teacher)

    def get(self, request, chapter_id):
        Chapter.objects.get(pk=chapter_id).delete()
        return redirect('classroom:dashboard')


# class ContentCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
#     def test_func(self):
#         login_url = "accounts:login"
#         return (self.request.user.is_teacher)

#     model = Content
#     fields = '__all__'


class ContentCreate(LoginRequiredMixin, UserPassesTestMixin, views.View):
    def test_func(self):
        login_url = "accounts:login"
        return (self.request.user.is_teacher)

    def get(self, request, course_id, chapter_id):
        self.course_id = course_id
        self.chapter_id = chapter_id
        form = ContentCreateForm()
        return render(request, "classroom/content_create.html", {'form': form})

    def post(self, request, course_id, chapter_id):
        form = ContentCreateForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.course_name_id = chapter_id
            content.uploaded_by = request.user
            content.save()
        else:
            return render(request, "classroom/content_create.html",
                          {'form': form})

        return redirect('classroom:dashboard')


class StudentManage(LoginRequiredMixin, UserPassesTestMixin, views.View):
    def test_func(self):
        login_url = "accounts:login"
        return (self.request.user.is_teacher)

    def get(self, request):

        students = request.user.teacher.grades.student_set.order_by('roll_no')
        context = {"students": students}
        return render(request, "classroom/manage_students.html", context)


class DeleteUser(LoginRequiredMixin, UserPassesTestMixin, views.View):
    def test_func(self):
        login_url = "accounts:login"
        return (self.request.user.is_teacher)

    def get(self, request, user_id):
        User = get_user_model()
        User.objects.get(pk=user_id).delete()
        return redirect('classroom:student_manage')


class ToggleActive(LoginRequiredMixin, UserPassesTestMixin, views.View):
    def test_func(self):
        login_url = "accounts:login"
        return (self.request.user.is_teacher)

    def get(self, request, user_id):
        User = get_user_model()
        user = User.objects.get(pk=user_id)
        user.is_active = not user.is_active
        user.save()
        return redirect('classroom:student_manage')


class UpdateStudent(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        login_url = "accounts:login"
        return (self.request.user.is_teacher)

    model = Student

    fields = ('roll_no', 'grades')


class UpdateUser(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        user_id = int(self.request.path[-1])
        login_url = "accounts:login"
        return (self.request.user.pk == user_id)

    model = get_user_model()

    fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'gender',
        'mobile_number',
        'location',
    )
