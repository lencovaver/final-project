from django.contrib import admin

from .models import Place, PostJob, Position, Language, DrivingLicence, PositionCategory


class PostJobAdmin(admin.ModelAdmin):
    list_display = ["id", 'position', 'place', 'work_type', 'status', 'author']      # Zobrazovaná pole v seznamu
    list_filter = ['status']                    # Filtr pro archivaci
    actions = ['archive_selected_jobs']         # Přidání akce pro archivaci více inzerátů najednou

    def archive_selected_jobs(self, request, queryset):
        queryset.update(status="archived")
        for inzerat in queryset:
            inzerat.archived = not inzerat.archived
            inzerat.save()
        self.message_user(request, "Inzeráty byly úspěšně archivovány.")

    archive_selected_jobs.short_description = "Archivovat vybrané inzeráty"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ["state", "level"]


admin.site.register(Place)
admin.site.register(PostJob, PostJobAdmin)
admin.site.register(PositionCategory)
admin.site.register(Position)
admin.site.register(Language, LanguageAdmin)
admin.site.register(DrivingLicence)