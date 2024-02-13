from django.urls import path

from .views import ArticlesList

urlpatterns = [
    path('get_articles_list/', ArticlesList.as_view())
]
