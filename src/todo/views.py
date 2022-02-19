import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from calendar import day_name
from .models import Task
from .form import TaskForm

@login_required
def home(request):
    tasks = Task.objects.filter(user_id=request.user.id).all()
    curr_date = datetime.today()
    ctx = {
        "tasks" : tasks,
        'day' : day_name[curr_date.weekday()],
    }
    return render(request, template_name='home.html', context=ctx)

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['description']
        
        new_task = Task.objects.create(title=title, description=desc, user_id=request.user.id)
        new_task.save()
        
        return redirect('home')
    
    form = TaskForm()
    return render(request, template_name='add_task.html', context={'form' : form})

@login_required
def update_task(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    
    if form.is_valid():
        form.save()
        return redirect('home')
    
    return render(request, template_name='update_task.html', context={'form' : form})

@login_required
def complet_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = json.loads(request.POST['data'])['completed']
    task.save()
    return HttpResponse("update successfully")

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponse("deleted successfully")
