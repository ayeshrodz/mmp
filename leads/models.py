from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class CustomerLead(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField(default=0)
    id_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return (self.first_name + " " + self.last_name)