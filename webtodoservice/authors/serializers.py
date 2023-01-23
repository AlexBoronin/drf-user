<<<<<<< HEAD
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
=======
from rest_framework.serializers import HyperlinkedModelSerializer
>>>>>>> a6fdf1940d4fb5f280e2c6ee5172eafc6ef2be34
from .models import Author, Project, ToDo


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