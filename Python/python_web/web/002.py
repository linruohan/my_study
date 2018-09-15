import web

urls = (
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        return open(r'E:\\atom\\Python\\web\\123.html').read()  

class index:
    def GET(self):
        query = web.input()
        return query

class blog:
    def POST(self):
        data = web.input()
        return data

    def GET(self):
        # get the request head
        return web.ctx.env


if __name__ == "__main__":
    app.run()
