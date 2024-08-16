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

    def __str__(self):
        return self.group_name


class Product(BaseModel):
    name = models.CharField(max_length=500,unique=True)
    slug = models.SlugField(max_length=500,unique=True,blank=True)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='products')
    is_liked = models.BooleanField(default=False)


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


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    is_primary = models.BooleanField(default=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')


class Comment(BaseModel):
    comment = models.TextField()
    slug = models.SlugField(max_length=500,unique=True,blank=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_id)
        super(Comment, self).save(*args, **kwargs)


class Key(BaseModel):
    key_name = models.CharField(max_length=500,unique=True)

    def __str__(self):
        return self.key_name


class Value(BaseModel):
    value_name = models.CharField(max_length=500,unique=True)

    def __str__(self):
        return self.value_name


class Atribute(BaseModel):
    key_name = models.ForeignKey(Key,on_delete=models.CASCADE)
    value_name = models.ForeignKey(Value,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=500,unique=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='attributes')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.key_name)
        super(Atribute, self).save(*args, **kwargs)




