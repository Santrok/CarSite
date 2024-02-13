from rest_framework.generics import ListAPIView

from .models import Article
from .serializers import ArticleSerializer


# Create your views here.

class ArticlesList(ListAPIView):
    """Класс для формирования и отдачи
     сеарилизованных данных модели Article"""

    queryset = Article.objects.filter(is_published=True)
    serializer_class = ArticleSerializer
