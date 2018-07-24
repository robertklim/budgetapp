from django.shortcuts import get_object_or_404, render
from .models import Project

def project_list(request):
    return render(request, 'budget/project-list.html')

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    return render(request, 'budget/project-detail.html', {'project': project, 'expanse_list': project.expanses.all()})