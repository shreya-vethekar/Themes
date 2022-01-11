from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class SignUpView(TemplateView):
    template_name="app/company-signup.html"

class LoginView(TemplateView):
    template_name="app/company-login.html"

class DetailsView(TemplateView):
    template_name="app/company-detail.html"

class PeopleView(TemplateView):
    template_name="app/company-people.html"

class SettingsView(TemplateView):
    template_name="app/company-settings.html"

class TaskView(TemplateView):
    template_name="app/company-task.html"

class TaskDetailView(TemplateView):
    template_name="app/company-task-detail.html"