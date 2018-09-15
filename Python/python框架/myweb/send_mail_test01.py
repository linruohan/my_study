from django.core.mail import send_mail
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
send_mail('Subject here', 'Here is the message.', 'from@example.com',
    ['to@example.com'], fail_silently=False)
