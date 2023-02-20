from django.shortcuts import render,redirect,get_object_or_404
from .models import Project,Task
from django.contrib import messages
from .forms import ProjectForm , TaskForm
from django.db.models import Sum

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    projects_h = Project.objects.annotate(total_hours=Sum('tasks__hours'))
    context = {'tasks': tasks,
               'projects': projects,
               'projects_h':projects_h
               }
    
    return render(request, 'main.html', context)
    


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully.')
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)
    context = {'form': form, 'project': project}
    return render(request, 'edit_project.html', context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'project': project}
    return render(request, 'delete_project.html', context)

def add_task(request, project_id):
    project = Project.objects.get(id=project_id)
    print(project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('projects')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form, 'project': project})

def edit_task(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id)
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        # Update the task with data from the form
        task.name = request.POST['name']
        task.description = request.POST['description']
        task.hours = request.POST['hours']
        task.save()
        return redirect('projects')
    context = {'project': project, 'task': task}
    return render(request, 'edit_task.html', context)

def delete_task(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id)
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('projects')
    context = {'project': project, 'task': task}
    return render(request, 'delete_task.html', context)



# def project_hours(request):
#     projects = Project.objects.annotate(total_hours=Sum('tasks__hours'))

#     return render(request, 'main.html', {'projects': projects})