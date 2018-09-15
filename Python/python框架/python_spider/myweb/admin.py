from django.contrib import admin

# Register your models here.
from django.contrib import admin
from myweb.models import Tag, Question, Answer

admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
