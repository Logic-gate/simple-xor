#!/usr/bin/python
import sys, shelve, getpass, string, os, email
import smtplib, poplib
from email import parser
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

#For Simple XOR-Like
from itertools import izip, cycle
import random
import datetime
import time
import binascii
from Tkinter import Tk
from tkFileDialog import askopenfilename


from re import *

now = datetime.datetime.now()
today = datetime.date.today()
pat=compile('([A-Z]*[a-z]*[0-9]*)+@([A-Z]*[a-z]*[0-9]*)+.([A-Z]*[a-z]*[0-9]*)')


def ask(question):
	print "\r%s" %question,
	return sys.stdin.readline().strip()

def isGoodEmail(addr):
	return pat.search(addr)

def getUser():
	user=ask('Your email address: ')
	if isGoodEmail(user): 
		return user
	else:
		print 'Invalid email address, try again:'
		return getUser()

def getReceiver(lst):
	receiver=ask('To: ')
	if isGoodEmail(receiver): 
		lst.append(receiver)
		more=ask('More recipients?(Y/N)')
		if more=='Y' or more=='y':
			getReceiver(lst)
	else:
		print 'Invalid email address, try again:'
		return getReceiver(lst)

def getSubject():
	subject=ask('Subject: ')
	if len(subject)>0: return subject
	else:
		ans= ask('Proceed without subject?(Y/N) ')
		if ans=='N' or ans=='n':return getSubject()
		else: return '[No subject]'

def getPassword(user):
	password= getpass.getpass('enter password for account %s: '%user)
	return password


def sendMail(sender,receiver,subject,text,pwd,files):
	msg=MIMEMultipart()
	msg['From']=sender
	msg['To']=email.Utils.COMMASPACE.join(receiver)
	msg['Date']=email.Utils.formatdate(localtime=True)
	msg['Subject']=subject
	msg.attach(MIMEText(text))
	
	for f in files:
		part=MIMEBase('application', "octet-stream")
		part.set_payload(open(f,"rb").read())
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
		msg.attach(part)

	server=smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(sender[0:sender.find('@')] ,pwd)
	server.sendmail(sender, receiver, msg.as_string())
	server.quit()

	
def connect(uid,pwd):
	print 'Connecting...'
	pop_conn=poplib.POP3_SSL('pop.gmail.com')
	pop_conn.user(userid)
	pop_conn.pass_(password)
	print pop_conn.getwelcome()
	return pop_conn

def attach(files):
	Tk().withdraw()
	path=askopenfilename()
	files.append(path)
	more=ask('More attachments?(Y/N)')
	if more=='Y' or more=='y':
		attach(files)

def filess():

	list_ = ["email/data.in", "email/data.out", "email/key.in", "email/email.mail"] #You can define any path. The defualt directory is where xor_en.py is.
	for p in list_:
		open(p, 'w')
#this will insure clean files everytime you run it. 
	


#####################
##   XOR Formula   ##
##                 ##
#####################
def xor_en(ms, ke):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(ms, cycle(ke)))

#####################
##   Randomiser    ##
##                 ##
#####################
    
#string.digits add it instead of asscii_lowercase or uppercase.

def rand(size=[], chars=string.ascii_uppercase +  string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))




def composeMail(sender,password,re=0,msg=None):
	if re==0:#not a reply
		print 'Composing a new message...'
		receiver=[]
		getReceiver(receiver)
		subject=getSubject()
	else:# reply
		receiver=[msg['Return-Path'] ]#should be a list
		print 'replying to %s ...'% receiver
		subject='RE:'+msg['Subject']
	open_text = os.system("gedit email/email.mail")
	read_ = open("email/email.mail", 'r')
	read_to_msg = read_.read()
	read_.close()
	message= read_to_msg + "\nSent from LilyXOR\nLilyMail + Simple XOR-Like"	
	files=[]
	hasFile=ask('Do you have an attachment?(Y/N)')
	if hasFile=='Y' or hasFile=='y':
		attach(files)
		
	ans= ask('Ready to send?(Y/N)')
	if ans=='Y' or ans=='y':
		print 'sending...'
		sendMail(sender,receiver,subject,message,password,files)
		print 'email sent to ',receiver,' successfully!'
	else:
		print 'Message abandoned'

#####################
##    Encrypter    ##
##      Email      ##
#####################
def composeEncryptedMail(sender,password,re=0,msg=None):
	if re==0:#not a reply
		print 'Composing a new message...'
		receiver=[]
		getReceiver(receiver)
		subject=getSubject()
	else:# reply
		receiver=[msg['Return-Path'] ]#should be a list
		print 'replying to %s ...'% receiver
		subject='RE:'+msg['Subject']
		
		
	
	os.system("gedit email/data.in") #change 'gedit' with your text editor
	path_of_data_in = open("email/data.in", 'r') #path of data.in
	data_in = path_of_data_in.read()  #read the content
	path_of_data_in.close()  #close the file
	l = len(data_in)  #count the char
	for i in data_in:  
		key_in= rand(l)   #based on l randomise 
	path_of_key = open("email/key.in", "w") #path of key.in
	path_of_key.write(key_in) 
	path_of_key.close()
	xor_en_x = xor_en(data_in, ke=key_in) #Encryption
	path_of_out = open("email/data.out", "w")
	path_of_out.write(xor_en_x) #Write the encrypted data
	path_of_out.close()
	log_header= """Date: """ + str(now) + '\n'+ """
Original Message: """ + str(data_in) + """
Number of Characters: """ + str(l) + '\n'+ """
Key:""" + str(key_in) +  '\n'+ """ 
Encrypted Message: """+ str(xor_en_x) + """"""
	log = 'email/log.txt'
	log_data = open(log, "w")
	log_data.write("\n" + log_header + "\n" )
	log_data.close()
	print ("""The defualt waiting time is 3s""")
	time.sleep(3)
	os.system("gedit email/data.in email/data.out email/key.in email/log.txt") #change 'gedit' with your text editor	
	
	
	message = xor_en_x +"\n\n\n\nThis is and encrypted email.\nSent from LilyXOR\nLilyMail + Simple XOR-Like"	 #Encrypted message	
	files=[]
	hasFile=ask('Do you have an attachment?(Y/N)')
	if hasFile=='Y' or hasFile=='y':
		attach(files)
		
	ans= ask('Ready to send?(Y/N)')
	if ans=='Y' or ans=='y':
		print 'sending...'
		sendMail(sender,receiver,subject,message,password,files)
		print 'email sent to ',receiver,' successfully!'
	else:
		print 'Message abandoned'

def extractMessageBody(msg):
	for part in msg.walk():
		if part.get_content_type()=='text/plain':
			return part.get_payload()

def getThisMailAction(messages, num):
	print '[OPTIONS: reply, quit...]\n'
	global userid,password
	msg=messages[num]
	action=ask('command: ')
	if action=='reply':
		composeMail(userid,password,1,msg)
		getInsideAction(messages)
	elif action=='quit':	
		getInsideAction(messages)
	elif action=='help':
		print '[reply] reply this email \n [quit] quit reading this email\n'
		getThisMailAction(messages, num)
	else:
		print 'invalid command'
		getThisMailAction(messages, num)

n=0
def getNum():
	global n
	n=n+1
	return n

def chkAttach(messages,num):#save attachments
	#only PDF files are checked
	msg=messages[num]
	attached=False
	for part in msg.walk():
		if part.get_content_type().find('application/pdf')>-1: attached=True
	if attached:	
		print 'Attachment(s) found!'
		ans=ask('Want to download?(Y/N)')
		if ans=='Y' or ans=='y':
			path=ask('Specify a path to save:')
			for part in msg.walk():
				ctype=part.get_content_type()
				if ctype.find('application/pdf')>-1:
					ext=ctype[ctype.find('/')+1:]
					fullpath=path+str(getNum())+'.'+ext
					open(fullpath,"wb").write(part.get_payload(decode=True))
					print 'Attachment saved to %s !' %fullpath

def getInsideAction(messages):
	print '[OPTIONS: ls, open, new, quit, newEn...]\n'
	global userid,password
	action=ask('command: ')
	if action=='ls':
		print 'Inbox: %s' % len(messages)
		i=0
		while i<len(messages): 
			print '['+str(i+1)+'] ',messages[i]['subject']
			i=i+1
		getInsideAction(messages)
	elif action=='quit':	
		#pop_conn.quit()
		userid='' #clear the data
		password=''
		print 'You are logged out'
		getAction()
	elif action=='new':
		composeMail(userid,password)
		getInsideAction(messages)
	elif action == 'newEn': #Encrypt new message
		composeEncryptedMail(userid,password)
		getInsideAction(messages)
	elif action=='open':
		index=int(ask("please specify the mail number: "))
		if 0<index<=len(messages):
			print '#'*64
			print 'SUBJECT:',messages[index-1]['Subject']
			print 'FROM:',messages[index-1]['From']
			print 'DATE:',messages[index-1]['Date']
			print '-'*24+'message below'+'-'*26+'\n'
			print extractMessageBody(messages[index-1])
			print '#'*64
			chkAttach(messages,index-1)#check attachments
			getThisMailAction(messages, index-1)
		else:
			print 'number out of range!'
			getInsideAction(messages)
	elif action=='help':
		print '[quit] exit login \n [new] compose new email\n [ls] list out mails in mailbox\n [open] open an email'
		getInsideAction(messages)
	else:
		print 'invalid command'
		getInsideAction(messages)

def readMail(pop_conn): #get msg from server
	msgs= [pop_conn.retr(i) for i in range(1,len(pop_conn.list()[1])+1)  ]
	msgs=['\n'.join(m[1]) for m in msgs]
	msgs= [parser.Parser().parsestr(m) for m in msgs] #a list of raw messages
	pop_conn.quit() ##maybe later?
	return msgs


def login():
	global userid, password  ### maybe global is not a good solution?
	userid=getUser()
	password=getPassword(userid)
	connection = connect(userid,password)
	messages=readMail(connection)
	getInsideAction(messages)


def getAction():
	print '[OPTIONS: login, quit...]\n'
	action=ask('command: ')
	if action=='quit':
		sys.exit(0)
	elif action=='login':
		print 'Please verify your identity '
		login()
	elif action=='help':
		print '[login] start a login session\n [quit] exit program'
	else:
		print 'invalid command'


if __name__=='__main__':
	print '\nLilyXOR 0.0.1 beta \n LilyMail by: Xiaolong Cheng \n Simple XOR-Like by: Ammer Madani(mad_dev)' 
	print 'Only encrypts outgoing emails'
	filess()
	userid=''
	password=''
	while True:
		getAction()

