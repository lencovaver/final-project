from django.contrib import admin

from .models import Place, PostJob,Position

# Register your models here.
admin.site.register(Position)
admin.site.register(Place)
admin.site.register(PostJob)

