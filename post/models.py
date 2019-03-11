from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default='')
    text = models.TextField()
    image = models.ImageField(upload_to='news', default='images/noimagefound.jpg')
    created_date = models.DateTimeField(
            default=timezone.now)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class News(Post):

    def __str__(self):
        return self.title


class Vacancy (Post):
    salary = models.IntegerField(default=0)
    company = models.CharField(max_length=64, default='')
    city = models.CharField(max_length=64, default='')
    address = models.CharField(max_length=128, default='')
    experience = models.IntegerField(default=0)



    def __str__(self):
        return self.title


class Shop (Post):
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.title