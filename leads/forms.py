from django import forms
from django.forms import fields
from .models import CustomerLead


class CustomerLeadModelForm(forms.ModelForm):
    class Meta:
        model = CustomerLead
        # fields = ("__all__")
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )


class CustomerLeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)