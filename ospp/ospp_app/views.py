from django.shortcuts import render
from ospp_app.models import User, Project, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def projects(request):
	projects = Project.objects.order_by('-date_create').filter(archive=False)
	archive = Project.objects.order_by('-date_create').filter(archive=True)

	for obj in projects:
		obj.comments = Comment.objects.filter(project=obj)
		# obj.files = File.objects.filter(project=obj).count()

	return render(request, 'projects.html', {'projects': projects, 'archive': archive})

@login_required
def archive(request):
	archive = Project.objects.order_by('-date_create').filter(archive=True)
	projects = Project.objects.order_by('-date_create').filter(archive=False)

	for obj in archive:
		obj.comments = Comment.objects.filter(project=obj)

	return render(request, 'archive.html', {'archive': archive, 'projects': projects})