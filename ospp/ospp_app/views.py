from django.shortcuts import render, HttpResponseRedirect
from ospp_app.models import User, Project, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from ospp_app.forms import CreateUserForm


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


def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
            new_user.save()
            new_user = authenticate(username=form.data['username'], password=form.data['password'])
            login(request, new_user)
            return HttpResponseRedirect('/projects')
    else:
        form = CreateUserForm()
    return render(request, 'registration/signup.html', {'form': form})