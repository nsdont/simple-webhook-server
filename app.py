# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from datetime import datetime
from tornado.options import define, options

define("port", default=3000, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('OK')
        print("-------- request logger start ---------")
        print(str(self.request.headers))
        print(self.request.body)
        print("-------- request logger end ---------")

    def post(self, *args, **kwargs):
        self.write('OK')
        print("-------- request logger start ---------")
        print(str(self.request.headers))
        print(self.request.body)
        print("-------- request logger end ---------")


def make_app():
    return tornado.web.Application([
        (r"(.*)", MainHandler),
    ])


if __name__ == "__main__":
    options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
