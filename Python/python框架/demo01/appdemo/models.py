from django.db import models

# Create your models here.
class Mysite(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField()
    author=models.CharField(max_length=100)
    num=models.IntegerField()
    def __str__(self):
        return self.title
    class Meta:#排序方式
        ordering=['num']
class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=40)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Author(models.Model):
    names=models.CharField(max_length=40)
    qq=models.CharField(max_length=20)
    def __str__(self):
        return self.names
        
#查询结果封装
class BookManager(models.Manager):
    def get_book_count(self,keyword):
        return self.filter(title__icontains=keyword).count()
#查询对象封装
class PythonManager(models.Manager):
    def get_query_set(self):
        return super(PythonManager,self).get_query_set().filter(title__icontains='django')



class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ManyToManyField(Author)
    publisher=models.ForeignKey(Publisher,on_delete=None)
    objects=BookManager()
    python_objects=PythonManager()
    def __str__(self):
        return self.title
