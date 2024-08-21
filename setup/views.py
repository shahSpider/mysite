from django.shortcuts import render
from setup.models import Company
from django.views import generic
from django.urls import reverse
from setup.forms import SetupUserCreationForm

def home(request):
    company = Company.objects.get(company_name="Fashion 360")
    context = {
        "company": company
    }
    return render(request, 'setup/home.html', context)


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = SetupUserCreationForm

    def get_success_url(self) -> str:
        return reverse("setup:login")