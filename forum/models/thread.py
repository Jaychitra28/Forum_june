from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from .category import Category


class Thread(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(max_length=400)
    category = models.ForeignKey(
        Category, related_name="thread", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="thread"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "thread_detail",
            args=[
                self.pk,
            ],
        )
