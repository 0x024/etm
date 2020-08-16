import os,email,imaplib
from email.parser import BytesParser
from email.utils import parseaddr 
from lxml import etree
import time

global count
host = 'imap.qq.com'
user = 'zw97073966@qq.com' 
passwd = 'feaybkuahvcacajc'
conn = imaplib.IMAP4_SSL(host) 
conn.login(user,passwd) 
conn.select()
type,data=conn.search(None,'ALL')
email_list=data[0].split()
#print (email_list)
#print (email_list)
#email_list=list(reversed(data[0].split()))
def decode_str(s):
	try:
		subject=email.header.decode_header(s)
	except:
		return None
	sub_bytes=subject[0][0]
	sub_charset=subject[0][1]
	if None==sub_charset:
		subject=sub_bytes
	elif 'unknown-8bit'==sub_charset:
		subject=str(sub_bytes,'utf-8')
	else:
		subject=str(sub_bytes,sub_charset)
	return subject

def get_transfer():
	messy_content=open('messy.log')
	tidy_content=open('tidy.log','w')
	for s in messy_content:
		tidy_content.write(s.replace('&nbsp;','').replace('<a <a ','<a ').replace('(<a href="http://www.12306.cn">www.12306.cn</a>)','').replace('（<a href="http://www.12306.cn">www.12306.cn</a>)',''))
	tidy_content.close()
	messy_content.close()
	html =etree.parse('tidy.log')
	cotents=html.xpath('text()')
	#print (br_tags)
	line_chick=cotents[2].replace("\n",'')
	line_detail=cotents[3].replace("\n",'')
	#os.remove('tidy.html')
	#os.remove('messy.html')
	print (line_chick)
	#print (line_chick)

def get_subject(num):
	type,data=conn.fetch(num,'(RFC822)')
	msg=BytesParser().parsebytes(data[0][1])
	sub=decode_str(msg.get('subject'))
	print(sub)
	return sub

def get_from(num):
	type,data=conn.fetch(num,'(RFC822)')
	msg=BytesParser().parsebytes(data[0][1])
	sub=decode_str(msg.get('From'))
	return sub

	#print(sub)			

def get_date(num):
	type,data=conn.fetch(num,'(RFC822)')
	msg=BytesParser().parsebytes(data[0][1])
	sub=msg.get('Date')
	print(sub)
	return sub
	#print(num, decode_str(sub)) 

def get_content(num):
	print (num)
	type,data=conn.fetch(num,'(RFC822)')
	msg=BytesParser().parsebytes(data[0][1])
	for part in msg.walk():
		if not part.is_multipart():   
			charset = part.get_charset()
			contenttype = part.get_content_type()
			content=part.get_payload(decode=True)
			content=content.decode('GBK')
			#print (content)
			with open("messy.log","w") as f:
				f.write(content)
			#get_transfer()
		






if __name__ == '__main__':
	for count in email_list:
		#print("VVVVVVVV")
		print(int(count))
		org_addrs=get_from(email_list[int(count)])
		tar_addrs='"12306@rails.com.cn" <12306@rails.com.cn>'
		if org_addrs==tar_addrs:
			print("OOOOOO")
			get_content(email_list[int(count)])
			continue


				#get_content(email_list[30])`

		




		#print (isinstance(org_addrs,str))
		#if org_addrs==tar_addrs:
		#	print ('222')
		#else:
		#	print("111")

		
	#get_date(email_list[21])
	#get_subject(email_list[21])
	#get_content(email_list[21])
	#get_subject(newlist[3],conn)
		#for part in msg.walk():
		#	if not part.is_multipart():
		#		print(part.get_payload(decode=True).decode('utf-8'))
	#conn.close()
	#conn.logout()
