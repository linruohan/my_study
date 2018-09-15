import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
django.setup()
'''one'''
from blog.models import Category, Tag, Post
# c = Category(name='category test01')
# c.save()
# t = Tag(name='tag test')
# t.save()
'''two'''
from django.utils import timezone
from django.contrib.auth.models import User

user = User.objects.get(username='mao')
print(user)
c = Category.objects.get(name='category test01')
p = Post(title='title test', body='body test', created_time=timezone.now(), modified_time=timezone.now(), category=c, author=user)
p.save()
print(c)
print(p.created_time)
print(p.modified_time)