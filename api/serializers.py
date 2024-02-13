from rest_framework import serializers

from .models import Article, ImageArticle


class ImageArticleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ImageArticle"""

    class Meta:
        model = ImageArticle
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Article"""

    images = ImageArticleSerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'link', 'date', 'headTitle', 'keywords',
                  'description', 'title', 'img', 'source',
                  'subtitle', 'photoText', 'markup', 'images']
