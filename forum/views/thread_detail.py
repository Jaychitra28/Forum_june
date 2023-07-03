from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models.response import Response
from ..models.thread import Thread
# from django.contrib.auth.decorators import login_required


# class ThreadDetailView(DetailView):
#     model=Thread
#     context_object_name="thread"
#     template_name="thread/thread_detail.html"
@login_required
def detail(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    response = Response.objects.filter(thread=thread)
    context = {"thread": thread, "response": response}
    return render(request, "thread/thread_detail.html", context)
    