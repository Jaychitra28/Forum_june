from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from ..models.response import Response
from ..models.thread import Thread
from django.contrib.auth.decorators import user_passes_test


@login_required
@user_passes_test
def delete_response(request, thread_id,response_id, UserPassesTestMixin):
    response = get_object_or_404(Response, id=response_id, created_by=request.user)
    thread = get_object_or_404(Thread, id=thread_id)
    context = {"response": response, "thread": thread}
    if request.method == "POST":     
        response.delete()
        return redirect("thread_detail", thread_id=thread_id)
    return render(request, "thread/response_delete.html", context)


