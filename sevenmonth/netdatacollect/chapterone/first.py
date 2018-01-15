# coding=utf8
from urllib import urlopen

from BeautifulSoup import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')


bsobj = BeautifulSoup(html)

namelist = bsobj.findAll('span', {'class':'green'})
print namelist
for name in namelist:
    print name.get_text()