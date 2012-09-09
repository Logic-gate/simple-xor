#!/usr/bin/python

from itertools import izip, cycle
import string
import random
import re
import math
import datetime
import os
import time
import binascii
from Tkinter import Tk
from tkFileDialog import askopenfilename



now = datetime.datetime.now()

#####################
##  File Creation  ##
##                 ##
#####################

def files():

	list_ = ["en/data.in", "en/data.out", "en/key.in", "de/de_data.in", "de/de_data.out", "de/de_key.in"] #You can define any path. The defualt directory is where xor_en.py is.
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


#####################
##    Encrypter    ##
##                 ##
#####################

def en():
	print """Place your message in the data.in tab, save it and then exit gedit"""
	os.system("gedit en/data.in") #change 'gedit' with your text editor
	path_of_data_in = open("en/data.in", 'r') #path of data.in
	data_in = path_of_data_in.read()  #read the content
	path_of_data_in.close()  #close the file
	l = len(data_in)  #count the char
	for i in data_in:  
		key_in= rand(l)   #based on l randomise 
	path_of_key = open("en/key.in", "w") #path of key.in
	path_of_key.write(key_in) 
	path_of_key.close()
		
		
		
	xor_en_x = xor_en(data_in, ke=key_in)
	de_xor_x = xor_en(xor_en_x, ke=key_in)
		
	path_of_out = open("en/data.out", "w")
	path_of_out.write(xor_en_x)
	path_of_out.close()
		
		
	log_header= """Date: """ + str(now) + '\n'+ """
Original Message: """ + str(data_in) + """
Number of Characters: """ + str(l) + '\n'+ """
Key:""" + str(key_in) +  '\n'+ """ 
Encrypted Message: """+ str(xor_en_x) + """"""
	log = 'en/log.txt'
	log_data = open(log, "w")
	log_data.write("\n" + log_header + "\n" )
	log_data.close()
	
	
	os.system("gedit en/data.in en/data.out en/key.in en/log.txt") #change 'gedit' with your text editor	

#####################
##    Encrypter    ##
##      File       ##
#####################

def en_file():
	print "Select the encrypted file"
	Tk().withdraw()
	path_of_file_data_in_en = askopenfilename()

	path_of_data_in = open(path_of_file_data_in_en, 'r') #path of data.in
	data_in = path_of_data_in.read()  #read the content
	path_of_data_in.close()  #close the file
	l = len(data_in)  #count the char
	for i in data_in:  
		key_in= rand(l)   #based on l randomise 
	path_of_key = open("en/key.in", "w") #path of key.in
	path_of_key.write(key_in) 
	path_of_key.close()
		
		
		
	xor_en_x = xor_en(data_in, ke=key_in)
	de_xor_x = xor_en(xor_en_x, ke=key_in)
		
	path_of_out = open("en/data.out", "w")
	path_of_out.write(xor_en_x)
	path_of_out.close()
		
		
	log_header= """Date: """ + str(now) +  '\n'+ """
Original Message: """ + str(data_in) +  '\n'+ """
Number of Characters: """ + str(l) +  '\n'+ """
Key:""" + str(key_in) + '\n'+""" 
Encrypted Message: """+ str(xor_en_x) + """"""
	log = 'en/log.txt'
	log_data = open(log, "w")
	log_data.write("\n" + log_header + "\n" )
	log_data.close()
	
	
	os.system("gedit en/data.out en/key.in en/log.txt") #change 'gedit' with your text editor	

#####################
##    Decrypter    ##
##                 ##
#####################
		
def de():
	print "Select the encrypted file"
	Tk().withdraw()
	path_of_file_data_in_ = askopenfilename()

	path_of_de_data_in = open(path_of_file_data_in_, "r")
	de_data_in = path_of_de_data_in.read()
	path_of_de_data_in.close()
		
	print "Select the key"
	path_of_file_data_key_ = askopenfilename()
	path_of_de_key = open(path_of_file_data_key_, "r")
	de_key_in = path_of_de_key.read()
	path_of_de_key.close()
		
	de_xor_x = xor_en(de_data_in, ke=de_key_in)
		
	path_of_de_data_out = open("de/de_data.out", "w")
	path_of_de_data_out.write(de_xor_x)
	path_of_de_data_out.close()
		
	
	log_header_de= """Date: """ + str(now) + """
Encrypted Message: """ + str(de_data_in) + """
Key:"""+str(de_key_in)+""" 
Decrypted Message: """+ str(de_xor_x)+ """\n"""
	log_de = 'de/log.txt'
	log_data_de = open(log_de, "w")
	log_data_de.write(log_header_de + "\n" )
	log_data_de.close()
	
	
	os.system("gedit de/log.txt de/de_data.out")


#####################
##    Encrypter    ##
##      File       ##
##	  Deprecated   ##
#####################

'''
def enf():
	Tk().withdraw()
	path_of_file = askopenfilename() 
	
	data_in_file = open(path_of_file, "rb")
	fen = data_in_file.read()
	data_in_file_hex = binascii.hexlify(fen)
	
	path_of_data_in_file = open("en/data.in", 'w')
	path_of_data_in_file.write(data_in_file_hex)
	data_in_file.close()
	path_of_data_in_file.close()
	path_of_data_in_file = open("en/data.in", 'r')
	
	data_file = path_of_data_in_file.read()
	path_of_data_in_file.close()
	

	
	
	ld = len(data_file)
	print """this may take some time"""
	print ld
	key_ = rand(ld) 	 
	path_of_key_file = open("en/key.in", "w")
	path_of_key_file.write(key_)
	path_of_key_file.close()
		
	
		
	xor_en_x_file = xor_en(data_file, ke=key_)
		
	path_of_out_file = open("en/data.out", "w")
	path_of_out_file.write(xor_en_x_file)
	path_of_out_file.close()
		
		
	log_header= """Date: """ + str(now) + """
Original Message: """ + str(data_file) + """
Number of Characters: """ + str(ld) + """
Key:"""+str(key_)+""" 
Encrypted Message: """+ str(xor_en_x_file)+ """"""
	log_file = 'en/log.txt'
	log_data_file = open(log_file, "w")
	log_data_file.write("\n" + log_header + "\n" )
	log_data_file.close()
	
	os.system("gedit en/data.in en/data.out en/key.in en/log.txt") #change 'gedit' with your text editor	


'''

def head_info():
	
	print "Simple XOR-Like 0.2 Beta\n" 
	print "0.2 beta:\nAdded file encryption(experimental)\nAdded main loop\nChenged name to Simple XOR-Like\nImplemented with email client: check LilyXOR.py\n"

	print ("""A simple XOR-Like Encrypter and Decrypter by mad_dev

This script will create the following:
"en/data.in", "en/data.out", "en/key.in", "de/de_data.in", "de/de_data.out", 
"de/de_key.in, "en/log.txt" and "de/log.txt"

All the files mentioned above will be opened in Gedit
(you can edit this from the source code)

NOTE: All files will be cleaned(erased) everytime you run this script""")

def cmd():
	msgs = """'e' for text encryption
'd' for text decryption
'ef' for for file encryption
'q' to quit"""
	print msgs


if __name__=='__main__':
	files()
	head_info()
	cmd()
	
	while True:
		c = raw_input(">> ")
		if c == "e":
			en()
		elif c == "d":
			de()
		elif c == "ef":
			en_file()
		#elif c == "enf":
		#	enf()
		elif c == "q":
			break
		else:
			cmd()
