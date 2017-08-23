# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
from datetime import datetime


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('OK')
        print("{} - {} - {} - {}".format(self.request.method,
                                         self.request.uri,
                                         self.request.body,
                                         datetime.now()))

    def post(self, *args, **kwargs):
        self.write('OK')
        print("{} - {} - {} - {}".format(self.request.method,
                                         self.request.uri,
                                         self.request.body,
                                         datetime.now()))


def make_app():
    return tornado.web.Application([
        (r"(.*)", MainHandler),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(3000)
    tornado.ioloop.IOLoop.current().start()
