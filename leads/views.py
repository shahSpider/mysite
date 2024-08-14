from django.shortcuts import render
from django.http import HttpResponse
from leads.models import Lead, Agent

def home(request):
    leads = Lead.objects.all()
    context = {
        "company": "Fashion 349",
        "since": 2002,
        "vision": """
                        To inspire confidence and individuality through sustainable,
                        cutting-edge fashion that transcends trends, empowering every person to express their unique style
                        while fostering a positive impact on the world.
                """,
        "leads": leads
    }
    return render(request, 'leads/index.html', context)
