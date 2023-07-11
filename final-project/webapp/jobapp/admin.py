from django.contrib import admin

from jobapp.forms import PostJobForm
from .models import Place, PostJob, Position, Language, DrivingLicence


class PostJobAdmin(admin.ModelAdmin):
    form = PostJobForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ["state", "level"]


admin.site.register(Place)
admin.site.register(PostJob, PostJobAdmin)
admin.site.register(Position)
admin.site.register(Language, LanguageAdmin)
admin.site.register(DrivingLicence)