import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
django.setup()
from blog.models import Category, Tag, Post
c=Category.objects.get(name='category test01')
c.name='category name_new'
c.save()
print(Category.objects.all())
