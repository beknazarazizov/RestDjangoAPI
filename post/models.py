from django.contrib.auth.models import User
from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts',null=True,blank=True)
    tags=models.ManyToManyField(Tag,related_name='posts',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

