from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class City(models.Model):
    name_city = models.CharField(max_length=100)

    class Meta:
        ordering = ['name_city']

    def __repr__(self):
        return f"{self.name_city}"

    def __str__(self):
        return repr(self)

    class Meta:
        verbose_name_plural = ('Cities')


class Company(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    street = models.CharField(max_length=255, default="no_address")
    num = models.CharField(max_length=10, blank=True, null=True)
    city = models.ForeignKey(City, related_name="companies", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ('Companies')

    def __str__(self):
        return self.name


class UserAgent(models.Model):
    agent_name = models.CharField(max_length=50, blank=False)
    agent_surname = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="Companies")
    area_code = models.CharField(max_length=4, blank=True, null=True, choices=[
        ("CZ", "+420"),
        ("SK", "+421"),
        ("CHE", "+41")
    ])
    phone = models.IntegerField(default="no_number")
    email = models.EmailField()


class UserPerson(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    area_code = models.CharField(max_length=4, blank=True, null=True, choices=[
        ("CZ", "+420"),
        ("SK", "+421"),
        ("CHE", "+41")
    ])
    phone = models.IntegerField(default="no_number")
    email = models.EmailField()

