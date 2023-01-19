from rest_framework.viewsets import ModelViewSet
from .models import Author, Project, ToDo
from .serializers import AuthorModelSerializer, ProjectModelSerializer, ToDoModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer

class MyAPIView(APIView):

    def get(self, request):
        return Response({'data': 'GET SUCCESS'})

    def get(self, request):
        return Response({'data': 'POST SUCCESS'})
