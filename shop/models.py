from django.db import models

class Shop(models.Model):
    title = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='shop', default='vacanse/noimagefound.jpg')
    text = models.CharField(max_length=500, default='')
    cost = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


