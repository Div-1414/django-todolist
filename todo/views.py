from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import todo


# Create your views here.
#view for adding task:-
def addtask(request):
    newtask=request.POST['task']
    todo.objects.create(task=newtask,user=request.user)
    
    return redirect('home')

#view for mark as done button:-
def mark_as_done(request,pk):
    task=get_object_or_404(todo,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

#view for mark as undone button:-
def mark_as_undone(request,pk):
    undonetask=get_object_or_404(todo,pk=pk)
    undonetask.is_completed=False
    undonetask.save()
    return redirect('home')

#view for deleting a task:-
def delete_task(request,pk):
    task=get_object_or_404(todo,pk=pk)
    task.delete()
    return redirect('home')

#views for editing task:-
def edit_task(request,pk):
    get_task=get_object_or_404(todo,pk=pk)
    
    if request.method=='POST':
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    else:
        context={
        'get_task':get_task,
    }
        return render(request,'edit_task.html',context)




    
