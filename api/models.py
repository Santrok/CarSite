from django.contrib import admin
from django.db import models


class Article(models.Model):
    """ Модель статей"""

    link = models.TextField(unique=True)
    date = models.DateField()
    headTitle = models.CharField(max_length=1000)
    keywords = models.TextField()
    description = models.TextField()
    title = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='articles_images')
    subtitle = models.CharField(max_length=1000)
    photoText = models.TextField()
    source = models.TextField()
    markup = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class ArticleAdmin(admin.ModelAdmin):
    """ Класс управления отображением
        в админ панели модели Article"""

    list_editable = ['is_published']
    list_display = ['title', 'is_published']
    list_filter = ['is_published']


class ImageArticle(models.Model):
    """ Модель изображений в статьях"""

    image = models.ImageField(upload_to='articles_images')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.article}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'