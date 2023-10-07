from django.conf import settings
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.title) + ', ' + str(self.author) + ', ' + str(self.publish_date)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.author) + ', ' + str(self.publish_date)
