#Python 2.7
# -*- coding: utf-8 -*-

import sys
import random

def decrypt():
	
	convert_list = {0:" ", 1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z", 27:"a", 28:"b", 29:"c", 30:"d", 31:"e", 32:"f", 33:"g", 34:"h", 35:"i", 36:"j", 37:"k", 38:"l", 39:"m", 40:"n", 41:"o", 42:"p", 43:"q", 44:"r", 45:"s", 46:"t", 47:"u", 48:"v", 49:"w", 50:"x", 51:"y", 52:"z", 53:"1", 54:"2", 55:"3", 56:"4", 57:"5", 58:"6", 59:"7", 60:"8", 61:"9", 62:"0", 63:"!", 64:"&", 65:"(", 66:")", 67:"=", 68:"?", 69:"Ã", 70:"Ÿ", 71:"+", 72:"*", 73:"~", 74:"-", 75:"â", 76:"€", 77:"“", 78:"_", 79:".", 80:",", 81:":", 82:";", 83:"<", 84:">", 85:"|"}
	print("Informations you want to decrypt")	
	data_raw = raw_input("->  ")
	data_binaries = ""
	data_output = ""
		
	for crypto_letter in data_raw:
		if crypto_letter in list0:
			data_binaries = data_binaries + "0"
		elif crypto_letter in list1:
			data_binaries = data_binaries + "1"
		
	number_check = 0 
	binary_string = '' 
	letter_id = 0
	
	for bin in data_binaries:
		if number_check < 8:
			number_check += 1
			binary_string = binary_string + bin
		if number_check == 8:
			number_check = 0
			if binary_string[0] == "1":
				letter_id += 128
			if binary_string[1] == "1":
				letter_id += 64
			if binary_string[2] == "1":
				letter_id += 32
			if binary_string[3] == "1":
	                        letter_id += 16
	                if binary_string[4] == "1":
	                        letter_id += 8
	                if binary_string[5] == "1":
	                        letter_id += 4
			if binary_string[6] == "1":
	                        letter_id += 2
	                if binary_string[7] == "1":
	                        letter_id += 1
	     		letter = convert_list[letter_id]
			data_output = data_output + letter
			letter_id = 0
			binary_string = ""
	
	print
	print "Decrypted Data ->"
	print
	print
	print data_output
	print 
	print  


def binaries(input):
	number = int(input)
	bin_100 = 256
	check_number = 0
	final_number = ""
	for id in range(8):
        	bin_100 = bin_100/2
		value_1 = number - bin_100
        	if value_1 >= 0:
                	final_number = final_number + ("1")
                	number = number - bin_100
        	else:               
                       final_number = final_number + ("0")

	return final_number


def encrypt():
	convert_list = {" ":"0", "A":"1", "B":"2", "C":"3", "D":"4", "E":"5", "F":"6", "G":"7", "H":"8", "I":"9", "J":"10", "K":"11", "L":"12", "M":"13", "N":"14", "O":"15", "P":"16", "Q":"17", "R":"18", "S":"19", "T":"20", "U":"21", "V":"22", "W":"23", "X":"24", "Y":"25", "Z":"26", "a":"27", "b":"28", "c":"29", "d":"30", "e":"31", "f":"32", "g":"33", "h":"34", "i":"35", "j":"36", "k":"37", "l":"38", "m":"39", "n":"40", "o":"41", "p":"42", "q":"43", "r":"44", "s":"45", "t":"46", "u":"47", "v":"48", "w":"49", "x":"50", "y":"51", "z":"52", "1":"53", "2":"54", "3":"55", "4":"56", "5":"57", "6":"58", "7":"59", "8":"60", "9":"61", "0":"62", "!":"63", "&":"64", "(":"65", ")":"66", "=":"67", "?":"68", "Ã":"69", "Ÿ":"70", "+":"71", "*":"72", "~":"73", "-":"74", "â":"75", "€":"76", "“":"77", "_":"78", ".":"79", ",":"80", ":":"81", ";":"82", "<":"83", ">":"84", "|":"85"}
	output_data = ""
	
	print("Information you want to encrypt")
	data_raw   = raw_input("->  ")
	data_lower = data_raw.lower()
	data_binaries = ""

	for letter in data_lower:
		letter_id = convert_list[letter]
		letter_binaries = binaries(letter_id)
		data_binaries = data_binaries + letter_binaries

	for number_bin in data_binaries:
		if number_bin == "1":
			id_list1 = random.randrange(0,30)
			output_data = output_data + list1[id_list1]
		if number_bin == "0":
			id_list0 = random.randrange(0,24)
			output_data = output_data + list0[id_list0]
	
	print
	print "Encrypted Data ->"
	print
	print
	print output_data
	print 
	print	


def help():
	print
	print("Encrypt and Decrypt your Data!")
	print
	print("Usage:")
	print("-e	Encrypt Informations")
	print("-d	Decrypt Informations")
	print("--info	Full Information to the Programm") 
	print

def info():
	print 
	print '''	This program is a cryptographie programm which uses a symmetric art of encryption.
	The keys of the ENCRYPTION are on one side the lists (lsit1, list0) which define which symbol a "0" 
	or a "1" should take and on the other hand the convertation lists, which define the value of an
	Letter (an integer).
	
	If you want to recommend something or want to give me feedback please contact me on GitHub!
	---xjmx---
	'''
	
#Main

list0 = ("-","_","1","2","3","7","w","e","r","z","o","p","a",")","[","x","v","b","m","+","'","{","}",":")
list1 = ("4","5","6","8","0","q","t","u","i","s","d","f","g","h","j","k","l","y","c",",",".","*","(","/","!","?",";","<",">","]")

try:	 
	usage = sys.argv[1];
except:
	usage = "-h"


checklist=("-d","-e","-h","--info")
if usage not in checklist:
	help()	
else:	
	if usage == "-d":
		decrypt()
	if usage == "-e":
		encrypt()
	if usage == "-h":
		help()
	if usage == "--info":
		info()








#Close
	
