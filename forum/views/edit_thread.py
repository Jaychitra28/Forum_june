from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from ..models.response import Response
from ..models.thread import Thread
from ..models.forms import EditThreadForm
from ..models.category import Category
from django.contrib.auth.decorators import user_passes_test

@login_required
@user_passes_test
def edit_thread(request, thread_id, category_id):
    thread = get_object_or_404(Thread, id=thread_id,created_by=request.user)
    category = get_object_or_404(Category, id=category_id)
  
    form = EditThreadForm(request.POST or None, instance=thread)
    if form.is_valid():
        thread = form.save(commit=False)
        thread.category = category
        thread.created_by = request.user
        thread.save()
        return redirect("thread_list", category_id=category_id)
    return render(request, "thread/edit_thread.html", {"thread": thread, "form":form})