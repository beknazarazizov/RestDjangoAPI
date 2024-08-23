from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from post.models import Post


#njdkdlf

@receiver(pre_save, sender=Post)
@receiver(post_save, sender=Post)
@receiver(post_delete, sender=Post)
def delete_saved_product(sender, instance, **kwargs):
    post_slug = kwargs.get('slug')
    tage_slug = kwargs.get('slug')
    cache.delete(f'post_list_{post_slug}_{tage_slug}')
    cache.delete(f'post_detail_{instance.id}')