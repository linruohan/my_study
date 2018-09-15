from django.contrib import admin

# Register your models here.
from people import models

admin.site.register(models.People)#把models中创建的表，添加到admin 后台中
