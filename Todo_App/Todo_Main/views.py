from django.shortcuts import render
from todo_list.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-created_at')
    completed_task = Task.objects.filter(is_completed=True)
    context = {
        'tasks': tasks,
        'is_completed': completed_task
    }
    return render(request, 'home.html', context)
