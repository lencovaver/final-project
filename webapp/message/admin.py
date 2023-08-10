from django.contrib import admin
from message.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "sender",
        "recipient",
        "content",
        "timestamp",
        "is_read",
        "is_archived",
    ]


admin.site.register(Message, MessageAdmin)
