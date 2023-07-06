from django.contrib import admin
from .models import Place, PostJob, Position

class PostJobAdmin(admin.ModelAdmin):
    list_display = ["positions", "place", "language", "accommodation", "salary", "diet"]

admin.site.register(Place)
admin.site.register(PostJob, PostJobAdmin)
admin.site.register(Position)