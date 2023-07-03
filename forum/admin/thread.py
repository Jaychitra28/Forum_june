from django.contrib import admin
from django.urls import reverse

from forum.models.thread import Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "description")
