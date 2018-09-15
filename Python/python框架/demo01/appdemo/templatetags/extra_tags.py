import datetime
#过滤器
from django import template
register=template.Library()

# @register.filter(name="cut")
# def myCut(value,arg):
#     return value.replace(arg,'*')

#{{current_time %Y-%m-%d %H:%M:%S}}
@register.tag(name="current_time")
def do_current_time(parser,token):
    try:
        tag_name,format_string=token.split_contents()
    except :
        raise  template.TemplateSyntaxError("syntax")
    return CurrentNode(format_string[1:-1])

class CurrentNode(template.Node):
    def __init__(self, s):
        self.format_string = str(s)

    def render(self,content):
        now=datetime.datetime.now()
        return now.strftime(self.format_string)
