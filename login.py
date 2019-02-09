#coding= utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web
from tornado.options import define,options
import json

from db import data
define("port",default = 8000,help ="run on the given port",type = int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("username","")
        password = self.get_argument("password", "")
        if len(username)==0:
            self.write("请输入用户名") 
            return
        if len(password)==0:
            self.write("请输入密码") 
            return
        D =data()
        res, email= D.checkusername('\"' + username + '\"')
        if res:
            self.render("information.html",userinfo = (username, password, email))
        else:
           self.write("username is error")      
        
    def post(self):
        username = self.get_argument("username","")
        password = self.get_argument("password", "")
        r = {"username":username}
        print r
        self.write(username)
        #self.write(json.dumps(r))
'''
        if len(username)==0:
            self.write("请输入用户名") 
            return
        if len(password)==0:
            self.write("请输入密码") 
            return
        D =data()
        res, email= D.checkusername('\"' + username + '\"')
        if res:
            print "email is " + email
            self.write("email is " + email) 
        else:
           self.write("username is error") 

'''
if __name__ =="__main__":
    tornado.options.parse_command_line()
    app =tornado.web.Application(handlers = [(r"/",IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
 
