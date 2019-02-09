#coding= utf-8
import MySQLdb

class data:
    def __init__(self):
        self.open_db =MySQLdb.connect(host ="47.254.80.179", user ="root", passwd ="password", db ="testmysql", charset ="utf8")
        self.cur = self.open_db.cursor()
        sql_db = "use testdb"
	self.cur.execute(sql_db)

    def creattable(self):  
        
        sql_createtable = "create table Person(usename char(20),personId int,mailadress char(20))"
        sql_insert ="insert into Person(usename,personId,mailadress) values('xiaoming',20190101,'xiaoming@126.com'),('John',20190102,'Joho2019@163.com'),('hangmeimei',20190103,'hangmeimei@163.com')"
        try:
            
            self.cur.execute(sql_createtable)
            self.cur.execute(sql_insert)
            self.open_db.commit()
   
        except Exception as e:
            print e
            self.open_db.rollback()
            
    def checkusername(self,user):
        sql_select = 'select usename,mailadress from Person where usename = ' + user
        self.cur.execute(sql_select)
        f= self.cur.fetchall()
        if len(f)==0:
            return False,0
            
        else:
            return True,f[0][1]
            
    
    
    def __del__(self):
        self.cur.close()
        self.open_db.close()
            
if __name__=="__main__":
    c =data()
        
    username = "uw"
    print c.checkusername('\"' + username + '\"')

    
