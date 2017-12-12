from bs4 import BeautifulSoup
import urllib2
import time
from dbconnect import connection

req = urllib2.urlopen('http://nationaljournal.com/politics?rss=1')

xml = BeautifulSoup(req, 'xml')# Error Video 7 de HTML

c, conn = connection()

for item in xml.findAll('link')[3:]:
    url = item.text
    c.execute("INSERT INTO links (time, link) VALUES (%s, %s)",
              (time.time(), url))
    conn.commit()

conn.close()
