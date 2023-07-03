from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models.forms import ResponseForm
from ..models.thread import Thread


@login_required
def home(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    form = ResponseForm(request.POST or None)
    if form.is_valid():
        response = form.save(commit=False)
        response.thread = thread
        response.created_by = request.user
        response.updated_by = request.user
        response.message=form.cleaned_data.get("message")
        response.save()
        return redirect("thread_detail", thread_id=thread_id)


    return render(request, "thread/create_response.html", {"thread": thread, "form": form})

