#coding=utf-8


class MyMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        print('12312312')
        super(MyMiddleware, self).__init__()
    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response
    def process_view(self,request,func,args,kwargs):
        print(func)
    # def process_request():
        # pass
    # def process_response():
    #     pass
    # def process_exception():
    #     pass
