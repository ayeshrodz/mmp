from django.urls import path
from leads.views import (
    customer_lead_list,
    customer_lead_detail,
    customer_lead_create,
)

app_name = "leads"

urlpatterns = [
    path('', customer_lead_list),
    path('<int:pk>/', customer_lead_detail),
    path('create/', customer_lead_create),
]