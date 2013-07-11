import urllib

from bottle import route, run, debug, view, template, CGIServer, error, redirect, post, request
from bottle import static_file

from config import *

from sqlCommon import *



@route('/static/:path#.+#')
def server_static(path):
	print path 
	print static_root
	return static_file(path, root=static_root)

@route('/:filename')
def server_test(filename):
	print filename
	return static_file(filename, root=server_root)


#@route('/favicon.ico')
#def sarve_test():
#	return static_file('favicon.ico', root=static_root)

@route('/')
@route('/index')
def index():
	return template("toolbar")

	

#a page use to compotie user infomation
@route('/adduserpage')
def adduserpage():
	return template("add-user")

#post is submit not route(405 method not allowed)

#adduser
@post('/add')
def addUser():
	username=request.forms.get('name')
	mail=request.forms.get('mail')
	password=request.forms.get('pwd')
	phone=request.forms.get('phone')
	address=request.forms.get('address')
	sql = "insert into mall.tb_user(username,password,email,phone,address) values('%s','%s','%s','%s','%s')" %(username,password,mail,phone,address)
	print sql
	mysql_insert(sql)
	
	return "success"

#show all user
@route('/showuser')
@view('show-user')
def showUser():
	sql="select id,username,email,phone,address from mall.tb_user"
	items=mysql_fetchall(sql)
	return dict({'items':items})	


#update user page
@route('/update')
def updateUser():
	return template("update")

#query one user infomation where you want change
@post('/queryUser')
@view('update-page')
def queryUser():
	username=request.forms.get('username')
	sql="select username,password,email,phone,address,id from mall.tb_user where username=('%s')" %(username)
	print sql
	item=mysql_fetchone(sql)
	print item
	if item is None:
		return "there found no infomation"
	return dict({"item":item})

#update user
@post('/updateUser')
def update():
	username=request.forms.get('username')
	password=request.forms.get('pwd')
	email=request.forms.get('email')
	phone=request.forms.get('phone')
	address=request.forms.get('address')
	sql="update mall.tb_user set password=('%s'),email=('%s'),phone=('%s'),address=('%s') where username=('%s')" %(password,email,phone,address,username)
	print sql
	mysql_update(sql)
	return "sucess"


#delete user
@post('/deleteUser')
def deleteUser():
	userid=request.forms.get('id')
	sql="delete from mall.tb_user where id=('%s')" %(userid)
	print sql
	mysql_delete(sql)
	return "sucess"



debug(True)
run( host='127.0.0.1', port=8080, reloader=True)
