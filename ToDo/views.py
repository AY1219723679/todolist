from django.shortcuts import render
from todolist.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'tasks': tasks,
    }
    print (tasks)
    return render(request,'home.html', context)