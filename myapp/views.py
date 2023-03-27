from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>"%username)

'''
def index(request, id):
    return HttpResponse("<h1>Index Page %s</h1>"%id)
'''

def index(request):
    title = 'DJANGO COURSE!!'
    return render(request, 'index.html',{
        'title': title,
    })

def projects(request):
    #projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)

    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

'''
def tasks(request, id):
    tasks = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s'%tasks.title)
'''

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=4)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'detail.html',{
        'project': project,
        'tasks': tasks
    })