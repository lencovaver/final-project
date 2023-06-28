from django.contrib import admin
from .models import Place, PostJob, Position


admin.site.register(Position)
admin.site.register(Place)
admin.site.register(PostJob)