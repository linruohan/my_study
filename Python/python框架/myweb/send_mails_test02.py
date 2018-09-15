from django.core.mail import send_mass_mail
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
'''备注：send_mail 每次发邮件都会建立一个连接，发多封邮件时建立多个连接。
而 send_mass_mail 是建立单个连接发送多封邮件，
所以一次性发送多封邮件时 send_mass_mail 要优于 send_mail。'''

message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])


send_mass_mail((message1, message2), fail_silently=False)
