from django.shortcuts import render
from projects.models import Project

# Create your views here.
def projects_index(request):
    projects = Project.objects.all()
    context = {'projects': projects }
    return render (request, 'projects_index.html', context)

def project_details(request, pk):
    projects = Project.objects.get(pk=pk)
    context = {"projects": projects}
    return render(request,"project_detail.html",context)
