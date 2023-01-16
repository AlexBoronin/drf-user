from django.db import models
from uuid import uuid4


class Author(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField()

class ToDo(models.Model):
    descript = models.TextField()
    dedline = models.DateField()

class Project(models.Model):
    title = models.CharField(max_length=32)
    executor = models.CharField(max_length=64)


