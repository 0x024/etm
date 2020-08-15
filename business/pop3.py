
import os,sys,string
import imaplib,email

attachementdir=r"d:\a"

host='imap.qq.com'
username='97073966@qq.com'
password='feaybkuahvcacajc'

conn=imaplib.IMAP4_SSL(host)
conn.login(username,password)


conn.list()
conn.select('INBOX')

result,dataid=conn.uid('search',None,'ALL')


mailidlist = dataid[0].split () 


def get_body(msg):
	if msg.is_mutipart():
		return get_body(msg.get_payload(0))
	else:
		return msg.get_payload(None,decode=True)

def search(key,value,conn):
	result , data = conn.search(None,key,'"()"'.format(value))
	return data

def get_attachements(msg):
	for part in msg.walk():
		if part.get_content_maintype() == 'multipart':
			continue
		if part.get('Content-Disposition') is None:
			continue
		filename = part.get_filename()
 
		if bool(filename):
			filepath = os.path.join(attachementdir,filename)
			with open(filepath,'wb') as f:
				f.write(part.get_payload(decode=True))
for id in mailidlist:
	result , data = conn.fetch ( id , '(RFC822)' )  
	e = email.message_from_bytes ( data[0][1] )
	subject = email.header.make_header ( email.header.decode_header ( e['SUBJECT'] ) )
	mail_from = email.header.make_header ( email.header.decode_header ( e['From'] ) )
	print("subject is%s" % subject)
	print("send for%s" % mail_from)
	body = str ( get_body ( e ) , encoding='utf-8' )   
	print("msg%s" % body)
conn.logout()  