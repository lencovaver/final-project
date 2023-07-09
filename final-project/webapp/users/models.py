from django.contrib.auth.models import AbstractUser
from django.db import models

from jobapp.models import Language


class City(models.Model):
    name_city = models.CharField(max_length=100)

    class Meta:
        ordering = ['name_city']
        verbose_name_plural = ('Cities')

    def __repr__(self):
        return f"{self.name_city}"

    def __str__(self):
        return repr(self)


class Company(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    street = models.CharField(max_length=255, default="")
    num = models.CharField(max_length=10)
    city = models.ForeignKey(City, related_name="companies", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ('Companies')

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_useragent = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="Companies", blank=True, null=True)

    bio = models.CharField(max_length=500, blank=True, null=True)
    language = models.CharField(max_length=5, choices=Language.STATE_CHOICES, blank=True, null=True)
    lang_level = models.CharField(max_length=30, choices=Language.LEVEL_CHOICES, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, default="")

    area_code = models.CharField(max_length=20, blank=True, choices=[
       ("🇨🇿 Czechia", "🇨🇿 +420"),
       ("🇸🇰 Slovakia", "🇸🇰 +421"),
       ("🇨🇭 Switzerland", "🇨🇭 +41")
    ])
    phone_number = models.IntegerField(blank=True, null=True)


class UserAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="useragent")


class UserPerson(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="userperson")
