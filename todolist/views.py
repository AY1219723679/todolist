from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.shortcuts import render

# Create your views here.

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home') 

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home') 

def edit(request, pk):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=pk)
        context = {
            'task': task,
        }
        return render(request,'edit.html', context)
    
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        task.task = request.POST['task']
        task.save()
        return redirect('home')

def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home') 
