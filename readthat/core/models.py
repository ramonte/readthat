from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    photo = models.CharField(max_length=100, blank=True, null=True)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    genre = models.CharField(max_length=20)
    year = models.IntegerField(default=2017, blank=True, null=True)
    pages = models.IntegerField(default=0, blank=True, null=True)
    cover = models.CharField(max_length=100, blank=True, null=True)

class Forum(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    creation = models.DateTimeField()
    description = models.CharField(max_length=600)
    upvotes = models.IntegerField(default=0)

class Comentary(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=600)
    date = models.DateTimeField()
    upvotes = models.IntegerField(default=0)
