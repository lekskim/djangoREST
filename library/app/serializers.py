from rest_framework.serializers import ModelSerializer
from .models import Author, Biography, Article, Book


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorModelSerializer2(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name']
class BiographyModelSerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'

class ArticleModelSerializer(ModelSerializer):
    author = AuthorModelSerializer()
    class Meta:
        model = Article
        fields = '__all__'

class BookModelSerializer(ModelSerializer):
  #  author = AuthorModelSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'
