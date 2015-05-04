from django.contrib import admin
from ospp_app.models import Project, Comment, Image, User

# Register your models here.
class ProjectInline(admin.StackedInline):
	model = Image
	extra = 1


class ProjectAdmin(admin.ModelAdmin):
	fields = ['name', 'description', 'date_create', 'date_modified', 'proj_author', 'archive']
	inlines = [ProjectInline]
	list_filter = ['date_create']

admin.site.register(Project, ProjectAdmin)