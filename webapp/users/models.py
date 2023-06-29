from django.contrib.auth.models import AbstractUser
from django.db import models
from jobapp.models import Place


class User(AbstractUser):
    pass


class UserAgent(models.Model):
    agent_name = models.CharField(max_length=50, blank=False)
    agent_surname = models.CharField(max_length=50)
    company = models.CharField(max_length=255)
    phone = models.IntegerField(default="no_number")
    email = models.EmailField()


class UserPerson(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField(default="no_number")
    email = models.EmailField()


class Company(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, default="no_address")
    contact_person = models.CharField(max_length=255, blank=False, null=False)
    telephone_number = models.IntegerField(default="no_number")
    email = models.EmailField(max_length=60)
    place = models.ForeignKey("jobapp.Place", on_delete=models.PROTECT, related_name="companies")

    class Meta:
        verbose_name_plural = ('Companies')

    def __str__(self):
        return self.name
