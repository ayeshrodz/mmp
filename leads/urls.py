from django.urls import path
from leads.views import (customer_lead_list, customer_lead_detail,
                         customer_lead_create, customer_lead_update,
                         customer_lead_delete)

app_name = "leads"

urlpatterns = [
    path('', customer_lead_list),
    path('<int:pk>/', customer_lead_detail),
    path('create/', customer_lead_create),
    path('<int:pk>/update/', customer_lead_update),
    path('<int:pk>/delete/', customer_lead_delete),
]