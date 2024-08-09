from typing import Any

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category_title = models.CharField(max_length=500,unique=True)
    slug = models.SlugField(max_length=500,unique=True,blank=True)
    category_image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_title)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_title


class Group(BaseModel):
    group_name = models.CharField(max_length=500,unique=True)
    slug = models.SlugField(max_length=500,unique=True,blank=True)
    group_image = models.ImageField(upload_to='images/')
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.group_name)
        super(Group, self).save(*args, **kwargs)


class Product(BaseModel):
    name = models.CharField(max_length=500,unique=True)
    slug = models.SlugField(max_length=500,unique=True,blank=True)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    is_liked = models.BooleanField(default=False)
    comment_count = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0)
    attributes = {
        'key':'value'
    }
    primary_image = models.ImageField(upload_to='images/')
    image_list = models.FileField(upload_to='images/')

    @property
    def discounted_price(self) -> Any:
        if self.discount > 0:
            return self.price * (1 - (self.discount / 100.0))
        return self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


class Comment(BaseModel):
    comment = models.TextField()
    slug = models.SlugField(max_length=500,unique=True,blank=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_id)
        super(Comment, self).save(*args, **kwargs)


class Atribute(BaseModel):
    key_name = models.CharField(max_length=500,unique=True)
    value_name = models.TextField()
    slug = models.SlugField(max_length=500,unique=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='attributes')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.key_name)
        super(Atribute, self).save(*args, **kwargs)



class Key(BaseModel):
    key_name = models.CharField(max_length=500,unique=True)
    slug = models.SlugField(max_length=500,unique=True,blank=True,null=False)
    atribute = models.ForeignKey(Atribute,on_delete=models.CASCADE,related_name='keys')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.key_name)
        super(Key,self).save(*args, **kwargs)


class Value(BaseModel):
    value_name = models.CharField(max_length=500,unique=True)
    slug = models.SlugField(max_length=500,unique=True,blank=True,null=False)
    atribute = models.ForeignKey(Atribute,on_delete=models.CASCADE,related_name='values')







