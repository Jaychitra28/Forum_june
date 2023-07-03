from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.category import Category
from ..models.thread import Thread
from django.shortcuts import get_object_or_404,redirect

@login_required
def delete(request, thread_id, category_id):
    thread = get_object_or_404(Thread, id=thread_id,created_by=request.user)
    category = get_object_or_404(Category, id=category_id)
    context = {"thread": thread, "category": category}
    if request.method == "POST":
        thread.delete()
        return redirect("thread_list", category_id=category_id)
    return render(request, "thread/thread_delete.html", context)
    