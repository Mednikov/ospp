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


class Image(models.Model):
    class Meta():
        db_table = 'image'

    image = models.ImageField(max_length=100)
    project = models.ForeignKey(Project)


class Comment(models.Model):
    class Meta():
        db_table = 'comment'

    text = models.TextField()
    project = models.ForeignKey(Project)