from django.contrib import admin
from .models import User, City


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name"]


class CityAdmin(admin.ModelAdmin):
    list_display = ["name_city"]


admin.site.register(User, UserAdmin)
admin.site.register(City, CityAdmin)
