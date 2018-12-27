import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('welcome python1805')


if __name__ == '__main__':
    app=tornado.web.Application([
        (r'/',IndexHandler)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()