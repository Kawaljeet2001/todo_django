from django.shortcuts import render , redirect , HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):

    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect("/")

    context = {"tasks" : tasks , "form":form}
    return render(request , "tasks.html" , context)
    
def updatetask(request , slug):
    task = Task.objects.get(id = slug)

    form = TaskForm(instance = task)

    if request.method =="POST":
        form = TaskForm(request.POST , instance = task)
        if form.is_valid:
            form.save()
            return redirect("/")
    return render(request , "update_task.html" , {"form":form})

def delete_task(request , slug):
    item = Task.objects.get(id = slug)

    if request.method == "POST":
        item.delete()
        return redirect("/")

    return render(request , "delete.html" , {"item":item})