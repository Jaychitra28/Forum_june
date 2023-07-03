from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ("title",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         "thread_list",
    #         args=[
    #             self.pk,
    #         ],
    #     )
