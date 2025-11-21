from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TaskForm
from .models import Task


def task_list(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Task added.")
            return redirect("todos:task_list")
        messages.error(request, "Please fix the issues below.")

    tasks = Task.objects.all()
    return render(request, "todos/task_list.html", {"form": form, "tasks": tasks})


@require_POST
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    return redirect("todos:task_list")


@require_POST
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.info(request, "Task removed.")
    return redirect("todos:task_list")
