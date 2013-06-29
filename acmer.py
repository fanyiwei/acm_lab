import MySQLdb
from poj import poj
from hdoj import hdoj
from cf import cf

class acmer:

    def __init__(self):
        conn=MySQLdb.connect(host='localhost',user='root',passwd='000000',db='acm_lab')
        cur=conn.cursor()
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
        results=self.cur.fetchall()
        c = cf()
        solved_id = []
        for line in results:
            solved_id.append((c.find(line[1]), line[0]))
        sql = 'update acmer set cf_rating=%s where id=%s'
        self.cur.executemany(sql, solved_id)
        self.conn.commit()
        print solved_id

    def update_all(self):
        self.update_poj()
        self.update_hdoj()
        self.update_cf()

    def __del__(self):
        self.cur.close()
        self.conn.close()






