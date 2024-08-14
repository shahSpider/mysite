from django.shortcuts import render
from setup.models import Company

def home(request):
    company = Company.objects.get(company_name="Fashion 360")
    context = {
        "company": company
    }
    return render(request, 'setup/home.html', context)
