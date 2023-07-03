from django.contrib import admin

from forum.models.category import Category


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
