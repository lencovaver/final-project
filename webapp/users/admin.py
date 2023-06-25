from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "contact_person", "telephone_number", "email", "place"]


admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)


