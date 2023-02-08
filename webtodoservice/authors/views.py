<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c360f5a12526693d3881e2ab247d62c381240e1f
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, Project, ToDo
from .serializers import AuthorModelSerializer, ProjectModelSerializer, ToDoModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
from rest_framework.viewsets import ModelViewSet
from .models import Author, Project, ToDo
from .serializers import AuthorModelSerializer, ProjectModelSerializer, ToDoModelSerializer
>>>>>>> a6fdf1940d4fb5f280e2c6ee5172eafc6ef2be34
=======
>>>>>>> c360f5a12526693d3881e2ab247d62c381240e1f
=======
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, Project, ToDo
from .serializers import AuthorModelSerializer, ProjectModelSerializer, ToDoModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.renderers import JSONRenderer
>>>>>>> 81c4be1594c20201da833060961309f0c78174b3


>>>>>>> 05f150ccafc96feb969e60f18f546f530547b60f
class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    filterset_fields = ['firstname']
=======
>>>>>>> a6fdf1940d4fb5f280e2c6ee5172eafc6ef2be34
=======
    filterset_fields = ['firstname']
>>>>>>> c360f5a12526693d3881e2ab247d62c381240e1f
=======
    filterset_fields = ['firstname']
>>>>>>> 81c4be1594c20201da833060961309f0c78174b3

class ProjectModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> c360f5a12526693d3881e2ab247d62c381240e1f
=======
>>>>>>> 81c4be1594c20201da833060961309f0c78174b3
    serializer_class = ToDoModelSerializer


class MyAPIView(ViewSet):
    def list(self, request):
        authors = Author.objects.all()
        serialiser = AuthorModelSerializer(authors, many=True)
        return Response(serialiser.data)

    @action(detail=False, methods=['get'])
    def Пушкин(self, request):
<<<<<<< HEAD
        return Response({'data': 'Писатель'})

=======
<<<<<<< HEAD
<<<<<<< HEAD
        return Response({'data': 'Писатель'})
=======
    serializer_class = ToDoModelSerializer
>>>>>>> a6fdf1940d4fb5f280e2c6ee5172eafc6ef2be34
=======
        return Response({'data': 'Писатель'})
>>>>>>> c360f5a12526693d3881e2ab247d62c381240e1f
=======
        return Response({'data': 'Писатель'})
>>>>>>> 81c4be1594c20201da833060961309f0c78174b3
>>>>>>> 05f150ccafc96feb969e60f18f546f530547b60f
