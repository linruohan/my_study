from django.conf import settings
from django.core.mail import EmailMultiAlternatives
'''添加附件发送邮件'''

from_email = settings.DEFAULT_FROM_EMAIL
# subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
msg = EmailMultiAlternatives(subject, content, from_email, [to_addr])

msg.content_subtype = "html"

# 添加附件（可选）
msg.attach_file('./twz.pdf')

# 发送
msg.send()
