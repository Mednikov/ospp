from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from ospp_app.models import User, Project, Image, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from ospp_app.forms import CreateUserForm, EditUserForm, CreateProjectForm, UploadImageForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required
def projects(request):
    projects = Project.objects.order_by('-date_create').filter(archive=False, proj_author=request.user)
    archive = Project.objects.order_by('-date_create').filter(archive=True, proj_author=request.user)

    for obj in projects:
        obj.comments = Comment.objects.filter(project=obj)
        obj.images = Image.objects.filter(project=obj)
        obj.placeholder = obj.images.first

    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                user = User.objects.get(username=request.user.username)
                new_project = Project(name=form.data['project_name'], description=form.data['project_description'], proj_author=user)
                new_project.save()
                return HttpResponseRedirect('/projects/'+str(new_project.id))
    else:
        form = CreateProjectForm()

    return render(request, 'projects.html', {'projects': projects, 'archive': archive, 'form': form})


@login_required
def project_detail(request, project_id):

    project = get_object_or_404(Project, pk=project_id)
    if request.user == project.proj_author:
        project.images = Image.objects.filter(project=project).order_by('image')


        if request.method == 'POST':
            form = UploadImageForm(request.POST, request.FILES)
            if form.is_valid():
                pic = Image(image=request.FILES['image'], project=project)
                pic = form.save(commit=False)
                pic.save()
                return render(request, 'projects_detail.html', {'project': project, 'form': form})
        else:
            form = UploadImageForm()
        return render(request, 'projects_detail.html', {'project': project, 'form': form})

        # if request.method == 'POST':
        #     form = UploadImageForm(request.POST, request.FILES)
        #     if form.is_valid():
        #         handle_uploaded_file(request.FILES['image'])
        #         return render(request, 'projects_detail.html', {'project': project, 'form': form})
        # else:
        #     form = UploadImageForm()
        # return render(request, 'projects_detail.html', {'project': project, 'form': form})

    else:
        return render(request, 'access_denied.html')


@login_required     #delete this line later
def project_preview(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.user == project.proj_author:
        project.images = Image.objects.filter(project=project).order_by('image')

        paginator = Paginator(project.images, 1)
        page = request.GET.get('page')
        try:
            project.pages = paginator.page(page)
        except PageNotAnInteger:
            project.pages = paginator.page(1)
        except EmptyPage:
            project.pages = paginator.page(paginator.num_pages)

        return render(request, 'projects_preview.html', {'project': project})
    else:
        return render(request, 'access_denied.html')


@login_required
def archive(request):
    archive = Project.objects.order_by('-date_create').filter(archive=True, proj_author=request.user)
    projects = Project.objects.order_by('-date_create').filter(archive=False, proj_author=request.user)

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


@login_required
def settings(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            user.first_name = form.data['first_name']
            user.last_name = form.data['last_name']
            user.email = form.data['email']
            user.save()
            return HttpResponseRedirect('/settings')
    else:
        form = EditUserForm()
    return render(request, 'settings.html', {'form': form})