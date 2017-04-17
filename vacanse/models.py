from django.db import models


class Vacanse(models.Model):
    title = models.CharField(max_length=20,default='')
    description = models.CharField(max_length=100,default='')
    image = models.ImageField(upload_to='vacance', default='vacanse/noimagefound.jpg')
    company = models.CharField(max_length=30,default='')
    city = models.CharField(max_length=20,default='')
    address = models.CharField(max_length=80,default='')
    salary = models.IntegerField(default=0)
    experience = models.CharField(max_length=10,default='')
    text = models.CharField(max_length=500,default='')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title