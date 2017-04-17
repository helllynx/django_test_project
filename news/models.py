from django.db import models

class News(models.Model):
    title = models.CharField(max_length=70, default='')
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(upload_to='news', default='vacanse/noimagefound.jpg')
    text = models.TextField()
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.title


