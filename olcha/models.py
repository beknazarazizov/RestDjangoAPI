
from django.db import models
from django.utils.text import slugify

# Create your models here.
"""category, group, Image, Product, Comment, Atribute, key ,value
1. Categories

http://127.0.0.1:8000/olcha-uz/category

    - category_title,
    - category_slug,
    - category_image
2.Group

http://127.0.0.1:8000/olcha-uz/category/category_slug/

    - group_name
    - group_image
    - category_slug

3.Products

http://127.0.0.1.8000/olcha-uz/products

name
description
price
discount
image
slug
is_liked
comment_count
avg_rating
attributes = {

    key:value
}
primary_image 
image_list


"""


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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Comment(BaseModel):
    comment = models.TextField()
    slug = models.SlugField(max_length=500,unique=True,blank=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_id)
        super(Comment, self).save(*args, **kwargs)


class Atribute(BaseModel):
    key_name = models.CharField(max_length=500,unique=True)
    value_name = models.TextField()
    atribute_slug = models.SlugField(max_length=500,unique=True,blank=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.atribute_slug:
            self.atribute_slug = slugify(self.key)
        super(Atribute, self).save(*args, **kwargs)



class Key(BaseModel):
    key_name = models.CharField(max_length=500,unique=True)
    slug = models.SlugField(max_length=500,unique=True,blank=True)
    atribute_id = models.ForeignKey(Atribute,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.key_name)
        super(Key,self).save(*args, **kwargs)


class Value(BaseModel):
    value_name = models.CharField(max_length=500,unique=True)
    slug = models.SlugField(max_length=500,unique=True,blank=True)
    atribute_id = models.ForeignKey(Atribute,on_delete=models.CASCADE)







