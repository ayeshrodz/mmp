from django.contrib import admin

from .models import CustomerLead, User, Agent

admin.site.register(User)
admin.site.register(CustomerLead)
admin.site.register(Agent)
