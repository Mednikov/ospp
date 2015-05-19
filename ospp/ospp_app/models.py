from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Project(models.Model):
    class Meta():
        db_table = 'project'

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    proj_author = models.ForeignKey(User, null=True)
    date_modified = models.DateTimeField(default=datetime.datetime.now)
    date_create = models.DateTimeField(default=datetime.datetime.now)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.name



def project_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/proj_<id>/<filename>
    return 'proj_{0}/{1}'.format(instance.project.id, filename)

class Image(models.Model):
    class Meta():
        db_table = 'image'

    image = models.ImageField(upload_to=project_directory_path)
    project = models.ForeignKey(Project)



class Comment(models.Model):
    class Meta():
        db_table = 'comment'

    text = models.TextField()
    project = models.ForeignKey(Project)