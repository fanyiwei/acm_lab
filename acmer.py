import MySQLdb
from poj import poj
from hdoj import hdoj
from cf import cf
import time

class acmer:

    def __init__(self):
        conn=MySQLdb.connect(host='localhost',user='root',passwd='000000')
        cur=conn.cursor()
        try:
            conn.select_db('acm_lab')
        except:
            sql = 'create database acm_lab'
            cur.execute(sql)
            conn.select_db('acm_lab')
            cur = conn.cursor()
            sql = "create table acmer(id int not null primary key, name varchar(255) default '', poj_name varchar(255) default '', poj_solved int default 0, hdoj_name varchar(255) default '', hdoj_solved int default 0, cf_name varchar(255) default '', cf_rating int default 0, photo_url varchar(255) default '/var/www/photo/default.png')"
            cur.execute(sql)
        self.conn = conn
        self.cur = cur

    def update_poj(self):
        sql = 'select id, poj_name from acmer'
        self.cur.execute(sql)
        results=self.cur.fetchall()
        p = poj()
        solved_id = []
        for line in results:
            solved_id.append((p.find(line[1]), line[0]))
        sql = 'update acmer set poj_solved=%s where id=%s'
        self.cur.executemany(sql, solved_id)
        self.conn.commit()
        print solved_id

    def update_hdoj(self):
        sql = 'select id, hdoj_name from acmer'
        self.cur.execute(sql)
        results=self.cur.fetchall()
        h = hdoj()
        solved_id = []
        for line in results:
            solved_id.append((h.find(line[1]), line[0]))
        sql = 'update acmer set hdoj_solved=%s where id=%s'
        self.cur.executemany(sql, solved_id)
        self.conn.commit()
        print solved_id

    def update_cf(self):
        sql = 'select id, cf_name from acmer'
        self.cur.execute(sql)
        results = self.cur.fetchall()
        c = cf()
        solved_id = []
        for line in results:
            solved_id.append((c.find(line[1]), line[0]))
        sql = 'update acmer set cf_rating=%s where id=%s'
        self.cur.executemany(sql, solved_id)
        self.conn.commit()
        print solved_id

    def update_sum(self):
        sql = 'select id, poj_solved, hdoj_solved from acmer'
        self.cur.execute(sql)
        results = self.cur.fetchall()
        a = int(time.time() / 86400)
        day29 = a % 30
        print day29
        day0 = (day29+1) % 30
        for line in results:
            sum_solved = line[1] + line[2]
            sql = 'update sum_solved set day%s=%s where id=%s' % (day29, sum_solved, line[0])
            self.cur.execute(sql)
            self.conn.commit()
            sql = 'select * from sum_solved where id=%s' % line[0]
            self.cur.execute(sql)
            r = self.cur.fetchone()
            days = []
            for i in range(0, 30):
                days.append(r[(day0+i)%30+1]-r[day0+1]) 
            for i in range(2, 30):
                if days[i] < days[i-1]:
                    days[i] = days[i-1]
            print days
            result = ''
            for i in range(2, 30):
                result += str(days[i] - days[i-1]) 
                if i != 29:
                    result += ','
            print result
            sql = 'update acmer set sum30="%s" where id="%s"' % (days[29]-days[1], line[0])
            self.cur.execute(sql)
            sql = 'update acmer set sum_solved="%s" where id=%s' % (result, line[0])
            self.cur.execute(sql)
            self.conn.commit()

    def update_all(self):
        self.update_poj()
        self.update_hdoj()
        self.update_cf()
        self.update_sum()

    def __del__(self):
        self.cur.close()
        self.conn.close()


