from __future__ import unicode_literals
from time import time
from django.db import models
from django.utils import timezone


def get_upload_file_name(instance,filename):
    return "uploaded_files/%s_%s"%(str(time()).replace('.','_'),filename)



# Create your models here.
class Article(models.Model):
    title = models.TextField(max_length=254)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to = get_upload_file_name)



    def __unicode__(self):
        return self.title
    
    
class comment(models.Model):
    name = models.CharField(max_length=100,default='null')
    body  = models.TextField()
    pub_date = models.DateTimeField('date published',default = timezone.now())
    article = models.ForeignKey(Article)

