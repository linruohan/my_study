import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
django.setup()
from blog.models import Category, Tag, Post
p=Post.objects.all()
print(p)
p.delete()
print(Post.objects.all())

print(BASE_DIR)