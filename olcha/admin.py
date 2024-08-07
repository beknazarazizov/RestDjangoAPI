from django.contrib import admin

from olcha.models import Category, Product,Group,Comment,Atribute,Value,Key

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Atribute)
admin.site.register(Value)
admin.site.register(Key)
