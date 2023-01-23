<<<<<<< HEAD
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, Project, ToDo
from .serializers import AuthorModelSerializer, ProjectModelSerializer, ToDoModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
=======
from rest_framework.viewsets import ModelViewSet
from .models import Author, Project, ToDo
from .serializers import AuthorModelSerializer, ProjectModelSerializer, ToDoModelSerializer
>>>>>>> a6fdf1940d4fb5f280e2c6ee5172eafc6ef2be34


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
<<<<<<< HEAD
    filterset_fields = ['firstname']
=======
>>>>>>> a6fdf1940d4fb5f280e2c6ee5172eafc6ef2be34


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
<<<<<<< HEAD
    serializer_class = ToDoModelSerializer


class MyAPIView(ViewSet):
    def list(self, request):
        authors = Author.objects.all()
        serialiser = AuthorModelSerializer(authors, many=True)
        return Response(serialiser.data)

    @action(detail=False, methods=['get'])
    def Пушкин(self, request):
        return Response({'data': 'Писатель'})
=======
    serializer_class = ToDoModelSerializer
>>>>>>> a6fdf1940d4fb5f280e2c6ee5172eafc6ef2be34
