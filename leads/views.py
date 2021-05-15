from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomerLead


def customer_lead_list(request):
    customerLeads = CustomerLead.objects.all()
    context = {"leads": customerLeads}
    return render(request, "leads/customer_lead_list.html", context)


def customer_lead_detail(request, pk):
    customerLead = CustomerLead.objects.get(id=pk)
    context = {"lead": customerLead}
    return render(request, "leads/customer_lead_detail.html", context)


def customer_lead_create(request):
    return render(request, "leads/customer_lead_create.html")