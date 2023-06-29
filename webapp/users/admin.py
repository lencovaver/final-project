from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Company, UserAgent, UserPerson


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "contact_person", "telephone_number", "email", "place"]


class UserAgentAdmin(admin.ModelAdmin):
    list_display = ["agent_name", "agent_surname", "company", "phone", "email"]


class UserPersonAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "phone", "email"]


admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(UserAgent, UserAgentAdmin)
admin.site.register(UserPerson, UserPersonAdmin)
