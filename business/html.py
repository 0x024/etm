from lxml import etree
import os,re

fp=open('ticket.html','w')
lines=open('mind.tmp','r')
for s in lines:
#	print (s)
	fp.write(s.replace('&nbsp;','').replace('（<a href="http://www.12306.cn">www.12306.cn</a>)',''))
fp.close()
lines.close()
html =etree.parse('ticket.html')
br_tags=html.xpath('text()')
#print (br_tags)
line_chick=br_tags[2].replace("\n",'')
line_detail=br_tags[3].replace("\n",'')
