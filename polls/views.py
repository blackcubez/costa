from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import request, HttpResponse
from .models import Question
from .forms import QuestionForm
# Create your views here.

def poll_create(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponse("Created Succcessfully")
    return render(request, "polls/question/create.html", { "form": form })

def poll_list(request):
    question = get_list_or_404(Question)
    context = {
        "question": question
    }
    return render(request, "polls/question/list.html", context)

def poll_detail(request, id=None):
    detail = get_object_or_404(Question, id=id)
    context = {
        "detail": detail,
    }
    return render(request, "polls/question/detail.html", context)
    
def poll_update(request):
    
    return HttpResponse("update")

def poll_delete(request):

    return HttpResponse("delete")

