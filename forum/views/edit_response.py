from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from ..models.response import Response
from ..models.thread import Thread
from ..models.forms import EditResponseForm


@login_required
def edit_response(request, thread_id, response_id):
    response = get_object_or_404(Response, id=response_id, created_by=request.user)
    thread = get_object_or_404(Thread, id=thread_id)
    form = EditResponseForm(request.POST or None, instance=response)
    if form.is_valid():
        # response.message=form.cleaned_data.get("message")
        response = form.save(commit=False)
        response.thread = thread
        response.created_by=request.user
        response.updated_by=request.user
        response.save()
        return redirect("thread_detail", thread_id=thread_id)
    return render(request, "thread/edit_response.html", {"thread": thread, "form":form})


