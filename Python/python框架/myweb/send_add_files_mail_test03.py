# 为安全起见，你可以弄两个版本，一个纯文本(text/plain)的为默认的，另外再提供一个 html 版本的（好像好多国外发的邮件都是纯文本的）
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

subject = '来自自强学堂的问候'

text_content = '这是一封重要的邮件.'

html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'

msg = EmailMultiAlternatives(subject, text_content, from_email, [to@youemail.com])

msg.attach_alternative(html_content, "text/html")

msg.send()
