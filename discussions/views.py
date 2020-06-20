from django.shortcuts import render
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Question, Subject
from django.shortcuts import redirect
from . import forms
from django.core.paginator import Paginator


class Home(LoginRequiredMixin, views.View):
    def get(self, request):

        search_query = request.GET.get("search_query", "")
        if request.user.is_student:
            # user_subjects = [
            #     i.pk for i in request.user.student.grades.subject_set.all()
            # ]
            user_subjects = request.user.student.grades.subject_set.values_list(
                'id', flat=True)

        elif request.user.is_teacher:
            user_subjects = [request.user.teacher.subject_id]

        questions = Question.objects.order_by('-posted_at').filter(
            subject_id__in=user_subjects,
            question_title__icontains=search_query)

        paginator = Paginator(questions, 5)

        page = request.GET.get("page", "1")
        page = int(page)

        page = paginator.page(page)  # requested page

        questions = page.object_list

        # final_questions = []

        # for question in questions:

        #     if question.subject.pk in user_subjects:
        #         final_questions.append(question)

        # context = {"questions": final_questions}
        context = {"questions": questions, "page": page, 'title': "Discussion"}
        return render(request, "discussions/index.html", context)


class QuestionView(LoginRequiredMixin, views.View):
    def get(self, request, pk):

        question = Question.objects.get(pk=pk)

        context = {"question": question, 'title': "Question"}

        return render(request, "discussions/question_answer.html", context)


class AnswerView(LoginRequiredMixin, views.View):
    def get(self, request, pk):

        question_id = pk

        question_title = Question.objects.get(pk=question_id).question_title

        form = forms.AnswerForm()

        context = {
            'form': form,
            "question": question_title,
        }

        return render(request, "discussions/answer.html", context)

    def post(self, request, pk):
        question_id = pk
        question_title = Question.objects.get(pk=question_id).question_title

        form = forms.AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.posted_by = request.user
            answer.question = Question.objects.get(pk=question_id)
            answer.save()
            return redirect('discussions:question', pk=question_id)
        context = {
            'form': form,
            "question": question_title,
        }

        return render(request, "discussions/answer.html", context)


class AddQuestionView(LoginRequiredMixin, views.View):
    def get(self, request):
        if request.user.is_student:
            user_subjects = [
                (i.pk, i.course_name)
                for i in request.user.student.grades.subject_set.all()
            ]
        elif request.user.is_teacher:
            user_subjects = [
                (request.user.teacher.subject.course_name,
                 request.user.teacher.subject.course_pk),
            ]

        return render(request, "discussions/add_question.html",
                      {'subjects': user_subjects})

    def post(self, request):
        question_subject = Subject.objects.get(pk=str(request.POST["subject"]))
        posted_by = request.user

        question = Question(
            question_title=request.POST['question_title'],
            subject=question_subject,
            posted_by=posted_by,
            question_content=request.POST['question_content'],
        )

        question.save()

        return redirect('discussions:question', pk=question.pk)
