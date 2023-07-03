from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models.forms import ThreadForm
from .category import Category

@login_required
def create(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    form = ThreadForm(request.POST or None)
    if form.is_valid():
        thread = form.save(commit=False)
        thread.category = category
        thread.created_by = request.user
        thread.save()
        return redirect("thread_list", category_id=category.id)
    return render(request, "thread/create_thread.html", {"category": category, "form": form})




# @login_required
# def edit_thread(request, thread_id, category_id):
#     thread = get_object_or_404(Thread, id=thread_id,created_by=request.user)
#     category = get_object_or_404(Category, id=category_id)
  
#     form = EditThreadForm(request.POST or None, instance=thread)
#     if form.is_valid():
#         thread = form.save(commit=False)
#         thread.category = category
#         thread.created_by = request.user
#         thread.save()
#         return redirect("thread_list", category_id=category_id)
#     return render(request, "thread/edit_thread.html", {"thread": thread, "form":form})