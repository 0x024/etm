import sqlite3
import os,email,imaplib
from email.parser import BytesParser
from email.utils import parseaddr 
import time,re
import datetime
from script import Transfer
from script import Location




aaaa=1


host = 'imap.qq.com'
user = '97073966@qq.com' 
passwd = 'feaybkuahvcacajc'
raw_conn = imaplib.IMAP4_SSL(host) 
raw_conn.login(user,passwd) 
raw_conn.select()
type,data=raw_conn.search(None,'ALL')
email_list=data[0].split()

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




def get_subject(num):
	type,data=raw_conn.fetch(num,'(RFC822)')
	try:
		msg=BytesParser().parsebytes(data[0][1])
		sub=decode_str(msg.get('subject'))
		print(sub)
		return sub
	except TypeError:
		print ('empty-email')
	except UnicodeDecodeError:
		print ('hahah')
def get_from(num):
	type,data=raw_conn.fetch(num,'(RFC822)')
	try :
		msg=BytesParser().parsebytes(data[0][1])
		sub=decode_str(msg.get('From'))
		#print (sub)
		return sub

	except TypeError:
		print ('empty-email')
		#print(sub)			
	except UnicodeDecodeError:
		print ('hahah')
def get_date(num):
	type,data=raw_conn.fetch(num,'(RFC822)')
	try :
		msg=BytesParser().parsebytes(data[0][1])
		sub=msg.get('Date')
		#print(sub)
		return sub
	#print(num, decode_str(sub)) 
	except TypeError:
		print ('empty-email')
	except UnicodeDecodeError:
		print ('hahah')

def time_formate(email_time):
	mind_befor_CTS_time='Fri 10 Nov 2017 00:00:00 '
	mind_formate_time=datetime.datetime.strptime(mind_befor_CTS_time,"%a %d %b %Y %H:%M:%S ")	
	email_recive_CTS_time=email_time.replace("(CST)","").replace(",","").replace(" +0800","")
	email_formate_time=datetime.datetime.strptime(email_recive_CTS_time,"%a %d %b %Y %H:%M:%S ")
	if email_formate_time >= mind_formate_time:
		return '2'
	else:
		return '1'
def get_content(num):
	type,data=raw_conn.fetch(num,'(RFC822)')
	email_date=get_date(email_list[int(count)])
	try :
		msg=BytesParser().parsebytes(data[0][1])
		for part in msg.walk():
			if not part.is_multipart():   
				charset = part.get_charset()
				contenttype = part.get_content_type()
				content=part.get_payload(decode=True)
				content=content.decode('GBK')
				temp=time_formate(email_date)
				if temp=='1':
					print('该邮件使用的老的内容，现使用V1版本进行解析')
					Transfer.get_transfer_v1(content)
				elif temp=='2':
					print('该邮件使用的新的内容，现使用V2版本进行解析')
					Transfer.get_transfer_v2(content)

	except TypeError:
		print ('empty-email')
	except UnicodeDecodeError:
		print ('hahah')




'''if __name__ == '__main__':
	for count in email_list:
		#print("VVVVVVVV")
		print(int(count))
		org_addrs=str(get_from(email_list[int(count)]))
		#print (isinstance(org_addrs,str))
		tar_addrs="<12306@rails.com.cn>"
		if tar_addrs in  org_addrs:
			#aaaa=aaaa+1
			print("OOOOOO")
			get_content(email_list[int(count)])
			
			#print ("+++++++++++="+str(aaaa))
			continue'''

if __name__ == '__main__':
	count = 0
	while count < 530:
		print("******************part_1*********************")
		print("******************part_1*********************")
		print("******************part_1*********************")
		print("******************part_1*********************")
		print("******************part_1*********************")
		print("******************part_1*********************")
		print("******************part_1*********************")
		print('现在开始查询第'+str(count)+'封邮件')
		org_addrs=str(get_from(email_list[int(count)]))
		#print (isinstance(org_addrs,str))
		tar_addrs="<12306@rails.com.cn>"
		if tar_addrs in  org_addrs:
			print("已匹配到12306邮件，下一步解析该邮件")
			get_content(email_list[int(count)])
		count=count+1
		print("此邮件解析完毕了")
		print("~~~~~~~~~~~~~~~~~end~~~~~~~~~~~~~~~~~~~~~~~")
		#time.sleep(2)

#
#get_from(email_list[330])
#get_content(email_list[173])

	



				#get_content(email_list[30])`

		




		#print (isinstance(org_addrs,str))
		#if org_addrs==tar_addrs:
		#	print ('222')
		#else:
		#	print("111")

		
	#get_date(email_list[21])
	#get_subject(email_list[21])
	#get_content(email_list[21])
	#get_subject(newlist[3],raw_conn)
		#for part in msg.walk():
		#	if not part.is_multipart():
		#		print(part.get_payload(decode=True).decode('utf-8'))
	#raw_conn.close()
	#raw_conn.logout()