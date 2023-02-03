from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, Book, Article, Biography
from .serializers import AuthorModelSerializer, BookModelSerializer, ArticleModelSerializer, BiographyModelSerializer
from rest_framework.views import APIView


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    filterset_fields = ['first_name', 'last_name', 'birthday_year']

 #  def get_queryset(self):
 #       return Author.objects.filter(first_name__contains='Alex')


class BookModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer

#class MyAPIView(APIView):
#    def get(self, request):
#        return Response({'data':'GET SUCCESS'})

#    def post(self, request):
#       return Response({'data': 'POST SUCCESS'})


#class MyAPIView(CreateAPIView, ListAPIView):
    #renderer_classes = [JSONRenderer]
#    queryset = Author.objects.all()
#   serializer_class = AuthorModelSerializer

class MyAPIView(ViewSet):
    def list(self, request):
        authors = Author.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(serializer.data)
