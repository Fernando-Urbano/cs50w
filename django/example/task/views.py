from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    return render(
        request, "task/index.html",
        {
            "tasks": tasks
        }
    )

def add(request):
    return render(request, "task/add.html")

def adddjango(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(
                request,
                "task/adddjango.html",
                {
                    "form": form
                }
            )

    return render(
        request, "task/adddjango.html",
        {
            "form": NewTaskForm()
        }
    )
