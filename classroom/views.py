from django.shortcuts import render
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.shortcuts import resolve_url


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, views.View):

    template_url = "classroom/index.html"

    def test_func(self):
        login_url = "accounts:login"
        return self.request.user.is_student

    def get(self, request):
        return render(request, self.template_url)
