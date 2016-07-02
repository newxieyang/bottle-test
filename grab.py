#! python
# coding=UTF-8
from requests import session
from bs4 import BeautifulSoup
import sys
import writeFile

reload(sys)

sys.setdefaultencoding('UTF-8')
#sysCharType = sys.getfilesystemencoding()

def all():
	url = 'http://www.cnier.ac.cn/book/1507/'

	bs = askNet(url)

	fileName = "C:\\Python27\\" + getFileName(bs)

	attrs = bs.select('#list > dl > dd > a')

	attrLen = len(attrs)
	
	page = 0

	for i in range(attrLen):
		if i%500 == 0:
			page += 1
		
		hrf = url + attrs[i]['href']
		#print hrf
		content = getContent(hrf)
		writeFile.writeFile(fileName + str(page) + ".txt", content)

	print len(attrs)


def askNet(url):
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"}

	s = session()
	r = s.get(url, headers=headers)
	if r.status_code == 200:
		return BeautifulSoup(r.text.decode("UTF-8").encode("ISO-8859-1"), "html.parser")
	else:
		askNet(url)

def getFileName(bs):
	return bs.select("#info > h1")[0].text

def getContent(url):

	print url
	bs = askNet(url)
	#print bs
	title = bs.select(".bookname > h1")[0].text
	print title
	str = bs.select("#content")[0].text
	#print str
	return title + "\n" + str


all()
#getContent("http://www.cnier.ac.cn/book/1507/827002.html")
