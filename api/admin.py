from django.contrib import admin

from .models import Article, ImageArticle, ArticleAdmin

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(ImageArticle)
