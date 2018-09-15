#coding=utf-8
from ctypes import *
#windows
msvcrt=cdll.msvcrt
message_str=b"Hello world!"
msvcrt.printf(b"Testing:%s",message_str)
#linux
# libc=CDLL("libc.so.6")
# message_str="Hello World!\n"
# libc.printf("Testing:%s",message_str)
print(c_int(9))
print(c_char_p(b"hello"))
print(c_ushort(-5))
seitz=c_char_p(b"love the python3")
print(seitz)
print(seitz.value)


#c  struct
# struct beer_recipe{
# int amt_barley;
# int amt_warter;
# }
#python
# class beer_recipe(Structure):
#     _fields_={
#     ("amt_barley",c_int),
#     ("amt_warter",c_int),
#     }


#c  union
# union{
# long barley_long;
# int barley_int;
# char barley_char[8];
# }
#python union
class barley_amount(Union):
    _fields_=[
    ("barley_long",c_long),
    ("barley_int",c_int),
    ("barley_char",c_char * 8),
    ]
value = 11111
my_barley=barley_amount(int(value))
print(my_barley.barley_long, my_barley.barley_int, my_barley.barley_char)
print("barley amount as a long:%1d"%my_barley.barley_long)
print("barley amount as an int:%d"%my_barley.barley_long)
print("barley amount as a long:%s"%my_barley.barley_char)
