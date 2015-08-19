from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop


class Handler(RequestHandler):
    def get(self):
        self.write('Hola Mundo HTML!')

try:
    Application([('/$', Handler)]).listen(50000)
    IOLoop.instance().start()

except KeyboardInterrupt:
    exit()
