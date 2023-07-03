
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from forum.models.thread import Category, Thread

@login_required
def list(request, category_id):
    category = Category.objects.get(id=category_id)
    threads = Thread.objects.filter(category=category)
    context = {"category": category, "threads": threads}
    return render(request, "thread/thread_list.html", context)
