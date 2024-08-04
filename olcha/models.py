from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField
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
    category_title = models.CharField(max_length=50,unique=True)
    category_slug = models.SlugField(max_length=50,unique=True,blank=True)
    category_image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.slug = slugify(self.category_title)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_title
