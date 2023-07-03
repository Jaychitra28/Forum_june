from django.contrib import admin
from django.urls import reverse

from forum.models.response import Response


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ("message", "thread")
