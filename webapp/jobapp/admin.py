from django.contrib import admin
from .models import Place, PostJob, Position, Language, DrivingLicence


class PostJobAdmin(admin.ModelAdmin):
    list_display = ["positions", "place", "get_languages", "accommodation", "salary", "diet"]

    def get_languages(self, obj):
        return ", ".join([str(language) for language in obj.language.all()])
    get_languages.short_description = "Languages"


admin.site.register(Place)
admin.site.register(PostJob, PostJobAdmin)
admin.site.register(Position)
admin.site.register(Language)
admin.site.register(DrivingLicence)
