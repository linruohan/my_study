from django.db import models
#pygments高亮库
from pygments.lexers import get_all_lexers,get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from datetime import datetime

LEXERS=[item for item in get_all_lexers()]
LANGUAGE_CHOICES=sorted([(item[1][0],item[0])for item in LEXERS])
STYLE_CHOICES=sorted((item,item)for item in get_all_styles())


# Create your models here.
class Snippet(models.Model):

    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100,blank=True,default='')
    code=models.TextField()
    linenos=models.BooleanField(default=False)
    language=models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default='python')
    style=models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default='friendly')

    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted=models.TextField()
    class Meta:
        ordering=('created',)
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        lexer=get_lexer_by_name(self.language)
        linenos=self.linenos and 'table' or False
        options=self.title and {'title':self.title} or {}
        formatter=HtmlFormatter(style=self.style,linenos=linenos,full=True,**options)
        self.highlighted=highlight(self.code,lexer,formatter)
        super(Snippet, self).save(*args,**kwargs)

class EmailVerifyRecord(models.Model):
    email_choices = (
        ('register', u'注册'),
        ('forget', u'找回密码'),
    )
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=email_choices, max_length=10, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')