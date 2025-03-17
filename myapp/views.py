from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import App
from .forms import AppForm
from django.db.models import Q
# Create your views here.

def add_task(request):
    add_success = False
    added_task = None
    if request.method == "POST":
        form = AppForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            add_success = True
            added_task = new_task
            return render(
                request, 
                'add_task.html',
                {"form": form,
                "added_task": added_task,
                "add_success": add_success},
            )
    else:
        form = AppForm()
    return render(request, 'add_task.html',{"form": form, "added_task": added_task,"add_success": add_success})    


def search_task(request):
    page_number = request.GET.get("page", 1)
    query = request.GET.get("q", "").strip()
    if request.method == "POST":
        query = request.POST.get("q", "").strip()
        page_number = 1
    if query:
        result = App.objects.filter(Q(task__icontains=query) | Q(name__icontains=query))
    else:
        result = App.objects.all()
        
    all_tasks = App.objects.all()
    paginator = Paginator(result, 10)
    page_obj = paginator.get_page(page_number)
    return render(request, 'search_task.html', {"result": page_obj, "query": query, "all_tasks": all_tasks})

def edit_task(request, task_id, page_number):
    pn = request.GET.get("page", page_number)
    print(f"[DBG] edit_task {task_id}, {page_number}, {pn} <<<")
    success = False
    if request.method == "POST":
        print("POST request received")
        result = App.objects.get(id=task_id)
        task = request.POST.get('task', result.task)
        task_description = request.POST.get('task_description', result.task_description)
        name = request.POST.get('name', result.name)
        status = request.POST.get('status', result.status)
        if result.task != task or result.task_description != task_description or result.name != name or result.status != status:
            result.task = task
            result.task_description = task_description
            result.name = name
            result.status = status
            result.save()
            success = True
            print("Updated success")
         
    task_list = App.objects.all()
    paginator = Paginator(task_list, 10)
    page_number = request.POST.get("page", request.GET.get("page", page_number))
    page_obj = paginator.get_page(page_number)
    return render(request, 'edit_task.html', {"result": page_obj, "success": success, "updated_task_id": task_id})
    
def delete_task(request, task_id, page_number):
    print("delete task with ID:", task_id)
    if request.method == "POST":
        task_edit = get_object_or_404(App, id=task_id)
        task_edit.delete()
        return redirect("edit_task", task_id=task_id, page_number=page_number)