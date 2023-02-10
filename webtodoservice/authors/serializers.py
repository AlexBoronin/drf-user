from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Author, Project, ToDo
from rest_framework import serializers
from .models import Author, Books



class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'