from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        "regarding",
        "email_address",
        "name",
        "message_subject",
        "message",
        "message_date",
        "reply_sent",
    )

    ordering = ("message_date",)


admin.site.register(ContactUs, ContactUsAdmin)
