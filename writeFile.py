#coding:utf-8

#读取文件
def read(fileName):
	try:
		f = open(fileName, 'r')
		print f.read()
	finally:
		if f:
			f.close()
			

#按行读取文件
def readLines(fileName):
	print fileName
	try:
		f = open(fileName, 'r')
		for line in f.readlines():
			print(line.strip()) 
	finally:
		if f:
			f.close()

# 写文件
def writeFile(fileName, content):
	print fileName
	try:
		f = open(fileName, 'a')
		f.write(content)
	finally:
		if f:
			f.close()
			
writeFile('C:\\Python27\\README2.txt','hello...cullen')
