

import imaplib 
import email 
from email.parser import BytesParser
from email.utils import parseaddr 
host = 'imap.qq.com'
user = '97073966@qq.com' 
passwd = 'feaybkuahvcacajc'
mail_directory = 'INBOX' 
conn = imaplib.IMAP4(host) 
conn.login(user,passwd) 
conn.select(mail_directory)
status, data = conn.search(None, 'ALL')
email_list = list(reversed(data[0].split()))
def decode_str(s):
    try:
        subject = email.header.decode_header(s)
    except:
        # print('Header decode error')
        return None 
    sub_bytes = subject[0][0] 
    sub_charset = subject[0][1]
    if None == sub_charset:
        subject = sub_bytes
    elif 'unknown-8bit' == sub_charset:
        subject = str(sub_bytes, 'utf8')
    else:
        subject = str(sub_bytes, sub_charset)
    return subject 
def get_email(num, conn):
    typ, content = conn.fetch(num, '(RFC822)')
    msg = BytesParser().parsebytes(content[0][1])
    sub = msg.get('Subject')
    for part in msg.walk():  
        fileName = part.get_filename()  
        fileName = decode_str(fileName)
        if None != fileName:
            print('+++++++++++++++++++')
            print(fileName)
   
    print(num, decode_str(sub)) 
for num in email_list:
    get_email(num, conn)
conn.close() 
conn.logout()