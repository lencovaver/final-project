from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Company(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    contact_person = models.CharField(max_length=255, blank=False, null=False)
    telephone_number = models.IntegerField(default="no_number")
    email = models.EmailField(max_length=60)
    place = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name_plural = ('Companies')

    def __str__(self):
        return self.name


class UserAgent(models.Model):
    agent_name = models.CharField(max_length=50)
    agent_surname = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="Companies")
    phone = models.IntegerField(default="no_number")
    email = models.EmailField()


class UserPerson(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField(default="no_number")
    email = models.EmailField()



