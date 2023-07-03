from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.category import Category


class CategoryListView(LoginRequiredMixin,ListView):
    queryset = Category.objects.all()
    context_object_name = "categories"
    template_name = "thread/category.html"
