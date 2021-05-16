from django.shortcuts import render, redirect
from .models import CustomerLead
from .forms import CustomerLeadModelForm


def customer_lead_list(request):
    customerLeads = CustomerLead.objects.all()
    context = {"leads": customerLeads}
    return render(request, "leads/customer_lead_list.html", context)


def customer_lead_detail(request, pk):
    customerLead = CustomerLead.objects.get(id=pk)
    context = {"lead": customerLead}
    return render(request, "leads/customer_lead_detail.html", context)


def customer_lead_create(request):
    form = CustomerLeadModelForm()
    if request.method == "POST":
        form = CustomerLeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
    }
    return render(request, "leads/customer_lead_create.html", context)


def customer_lead_update(request, pk):
    customerLead = CustomerLead.objects.get(id=pk)
    form = CustomerLeadModelForm(instance=customerLead)
    if request.method == "POST":
        form = CustomerLeadModelForm(request.POST, instance=customerLead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {"form": form}
    return render(request, "leads/customer_lead_update.html", context)


def customer_lead_delete(request, pk):
    lead = CustomerLead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")


# def customer_lead_create(request):
#     # form = CustomerLeadForm()
#     form = CustomerLeadForm()
#     if request.method == "POST":
#         print("Receiving a post request")
#         #form = CustomerLeadForm(request.POST)
#         form = CustomerLeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             CustomerLead.objects.create(first_name=first_name,
#                                         last_name=last_name,
#                                         age=age,
#                                         agent=agent)
#         # print("The lead has been created")
#         return redirect("/leads")
#     context = {
#         "form": form,
#     }
#     return render(request, "leads/customer_lead_create.html", context)
