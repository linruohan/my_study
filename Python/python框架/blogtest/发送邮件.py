from django.core.mail import send_mail
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
django.setup()
send_mail(
    '邮件标题',
    '邮件内容',
    'mjt1220@126.com',
    ['mjt1220@126.com'],
)
subject, form_email, to = 'hello', 'from@example.com', '1565208411@qq.com'
text_content = 'This is an important message'
html_content = u'<b>激活链接：</b><a href="http://www.baidu.com">http:www.baidu.com</a>'
msg = EmailMultiAlternatives(subject, text_content, form_email, [to])
msg.attach_alternative(html_content, 'text/html')
msg.send()
