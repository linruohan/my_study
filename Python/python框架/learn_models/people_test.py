# -*- coding: utf-8 -*-
import os,django
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learn_models.settings")
django.setup()
from people.models import People

# People.objects.create(name='xiaohan',age=24)
xiaohan=People.objects.get(name='xiaohan')
s=People.objects.filter(name__icontains="xiao")
print(xiaohan.age)
print(s)

print(People.objects.all())
