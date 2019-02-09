#coding= utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web
from tornado.options import define,options

from db import data
define("port",default = 8000,help ="run on the given port",type = int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("username","")
        if len(username)==0:
            self.write("请输入用户名") 
            return
        D =data()
        res, email = D.checkusername('\"' + username + '\"')
        if res:
            self.write("email is:" + email)
        else:
            self.write("username is error")
            
    


if __name__ =="__main__":
    tornado.options.parse_command_line()
    app =tornado.web.Application(handlers = [(r"/",IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
    
