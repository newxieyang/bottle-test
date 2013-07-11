import MySQLdb
from config import *


##query more
def mysql_fetchall(sql):
        db=MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd,charset=mysql_charset)
        cur=db.cursor()
        cur.execute(sql)
        items=cur.fetchall()
        cur.close()
        db.close()

        return items

##query one
def mysql_fetchone(sql):
        db=MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd,charset=mysql_charset)
        cur=db.cursor()
        cur.execute(sql)
        item=cur.fetchone()
        cur.close()
        db.close()

        return item


## insert
def mysql_insert(sql):
        db=MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd,charset=mysql_charset)
        cur=db.cursor()
        try:
                cur.execute(sql)
		db.commit()
        except Exception,e:
                db.rollback()
                print e
        cur.close()
        db.close()

## delete
def mysql_delete(sql):
        db=MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd,charset=mysql_charset)
	cur=db.cursor()
	try:	
		cur.execute(sql)
		db.commit()
	except Exception,e:
		db.rollback()
		print e
	cur.close()
	db.close()

## update
def mysql_update(sql):
        db=MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_passwd,charset=mysql_charset)
        cur=db.cursor()
        try:
                cur.execute(sql)
		db.commit()
        except Exception,e:
                db.rollback()
                print e
        cur.close()
        db.close()


