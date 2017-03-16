from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='news')
    text = models.TextField()
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.title


