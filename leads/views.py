from django.shortcuts import render
from django.http import HttpResponse
from leads.models import Lead, Agent

def leads_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, 'leads/leads_list.html', context)


def leads_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, 'leads/leads_detail.html', context)


