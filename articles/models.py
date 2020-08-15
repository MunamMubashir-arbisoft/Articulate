from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(('slug'), max_length=50, unique=True, populate_from=('title',))
    description = models.CharField(max_length=300)
    content = models.TextField()

    # blank = True means not required in Django
    # null = True means not required in the database
    cover_image = models.ImageField(upload_to="images/article-cover/", blank=True, null=True)
    author = models.ForeignKey('profiles.Profile',
                               on_delete=models.CASCADE,
                               related_name='articles')
    tags = models.ManyToManyField('articles.Tag', related_name='tags', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey('profiles.Profile',
                               on_delete=models.CASCADE,
                               related_name='comments')

    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)