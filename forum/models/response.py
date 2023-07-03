from django.contrib.auth.models import User
from django.db import models

from .thread import Thread, Category


class Response(models.Model):
    message = models.TextField(max_length=4000)
    thread = models.ForeignKey(
        Thread, related_name="response", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        User, related_name="response", on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(
        User, null=True, related_name="+", on_delete=models.CASCADE
    )
