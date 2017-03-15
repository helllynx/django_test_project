from django.db import models

class News(models.Model):
    title = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='/media/news',height_field=100, width_field=150)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
