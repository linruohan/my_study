import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



snippet = Snippet(code='foo = "bar"\n')
snippet.save()
snippet = Snippet(code='print "hello, world"\n')
snippet.save()

# Model -> Serializer  序列化
serializer=SnippetSerializer(snippet)
print('serializer.data:',serializer.data)
# { 'pk':2, 'title':u'', 'code':u'print("hello,world")\n','linenos':2, 'language':2,'style':2,}
# Serializer -> JSON
content=JSONRenderer().render(serializer.data)
print('content:',content)

# stream -> json 反序列化
from django.utils.six import BytesIO
stream=BytesIO(content)
print(stream)
data = JSONParser().parse(stream)
print('data:',data)

# json -> serializer
serializer=SnippetSerializer(data=data)
serializer.is_valid()
#true
print(serializer.validated_data)
#OrderdDict([('title',''),('code','print"hello,world"\n'),(),()])
serializer.save
#<Snippet:Snippet object>
