from django import forms
from django.forms import fields
from .models import CustomerLead


class CustomerLeadModelForm(forms.ModelForm):
    class Meta:
        model = CustomerLead
        fields = ("__all__")
