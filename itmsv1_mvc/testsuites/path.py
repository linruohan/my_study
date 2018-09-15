import os
dir=os.path.dirname(__file__)
parent=os.path.dirname(os.path.dirname(__file__))
s=os.path.join(os.path.dirname(__file__),"..")
ss=os.path.abspath(parent)
print(os.path.dirname(os.path.dirname(__file__)))