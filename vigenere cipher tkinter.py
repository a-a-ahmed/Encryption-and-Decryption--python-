# importing tkinter module for GUI
from tkinter import *

# importing other required modules 
import random 
import time 
import datetime 

# creating a root object 
root = Tk() 

# defining the resolution of the window 
root.geometry("1200x6000") 

# the title of window 
root.title("Message Encryption and Decryption") 

Tops = Frame(root, width = 1600, relief = SUNKEN) 
Tops.pack(side = TOP) 

f1 = Frame(root, width = 800, height = 700, 
							relief = SUNKEN) 
f1.pack(side = LEFT) 

# displaying a welcome message and time

localtime = time.asctime(time.localtime(time.time())) 

lblInfo = Label(Tops, font = ('helvetica', 50, 'bold'), 
		text = "SECRET MESSAGING \n (using vigenere cipher) \n Adnaan Arbaaz Ahmed", 
					fg = "Black", bd = 10, anchor='w') 
					
lblInfo.grid(row = 0, column = 0) 

lblInfo = Label(Tops, font=('arial', 20, 'bold'), 
			text = localtime, fg = "Steel Blue", 
						bd = 10, anchor = 'w') 
						
lblInfo.grid(row = 1, column = 0) 

rand = StringVar() 
Msg = StringVar() 
key = StringVar() 
mode = StringVar() 
Result = StringVar() 

# exit function 
def qExit(): 
	root.destroy() 

# Function to reset the window

def Reset(): 
	rand.set("") 
	Msg.set("") 
	key.set("") 
	mode.set("") 
	Result.set("") 


# references

lblReference = Label(f1, font = ('arial', 16, 'bold'), 
				text = "NAME", bd = 16, anchor = "w") 
				
lblReference.grid(row = 0, column = 0) 

txtReference = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = rand, bd = 10, insertwidth = 4, 
						bg = "powder blue", justify = 'right') 
						
txtReference.grid(row = 0, column = 1) 

# labels

lblMsg = Label(f1, font = ('arial', 16, 'bold'), 
		text = "MESSAGE", bd = 16, anchor = "w") 
		
lblMsg.grid(row = 1, column = 0) 

txtMsg = Entry(f1, font = ('arial', 16, 'bold'), 
		textvariable = Msg, bd = 10, insertwidth = 4, 
				bg = "powder blue", justify = 'right') 
				
txtMsg.grid(row = 1, column = 1) 

lblkey = Label(f1, font = ('arial', 16, 'bold'), 
			text = "KEY", bd = 16, anchor = "w") 
			
lblkey.grid(row = 2, column = 0) 

txtkey = Entry(f1, font = ('arial', 16, 'bold'), 
		textvariable = key, bd = 10, insertwidth = 4, 
				bg = "powder blue", justify = 'right') 
				
txtkey.grid(row = 2, column = 1) 

lblmode = Label(f1, font = ('arial', 16, 'bold'), 
		text = "MODE\n(e for encrypt, d for decrypt)", 
								bd = 16, anchor = "w") 
								
lblmode.grid(row = 3, column = 0) 

txtmode = Entry(f1, font = ('arial', 16, 'bold'), 
		textvariable = mode, bd = 10, insertwidth = 4, 
				bg = "powder blue", justify = 'right') 
					
txtmode.grid(row = 3, column = 1) 

lblService = Label(f1, font = ('arial', 16, 'bold'), 
			text = "RESULT", bd = 16, anchor = "w") 
			
lblService.grid(row = 2, column = 2) 

txtService = Entry(f1, font = ('arial', 16, 'bold'), 
			textvariable = Result, bd = 10, insertwidth = 4, 
					bg = "powder blue", justify = 'right') 
						
txtService.grid(row = 2, column = 3) 

# Vigenère cipher 
import base64 

# Function for encoding 
def encode(key, clear): 
	enc = [] 
	
	for i in range(len(clear)): 
		key_c = key[i % len(key)] 
		enc_c = chr((ord(clear[i]) +
					ord(key_c)) % 256) 
					
		enc.append(enc_c) 
		
	return base64.urlsafe_b64encode("".join(enc).encode()).decode() 

# Function for decoding 
def decode(key, enc): 
	dec = [] 
	
	enc = base64.urlsafe_b64decode(enc).decode() 
	for i in range(len(enc)): 
		key_c = key[i % len(key)] 
		dec_c = chr((256 + ord(enc[i]) -
						ord(key_c)) % 256) 
							
		dec.append(dec_c) 
	return "".join(dec) 


def Ref(): 
	print("Message= ", (Msg.get())) 

	clear = Msg.get() 
	k = key.get() 
	m = mode.get() 

	if (m == 'e'): 
		Result.set(encode(k, clear)) 
	else: 
		Result.set(decode(k, clear)) 

# Show message button 
btnTotal = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", 
						font = ('arial', 16, 'bold'), width = 10, 
					text = "Show Message", bg = "green", 
						command = Ref).grid(row = 7, column = 1) 

# Clear button 
btnClear = Button(f1, padx = 16, pady = 8, bd = 16, 
				fg = "black", font = ('arial', 16, 'bold'), 
					width = 10, text = "Clear", bg = "aqua", 
				command = Reset).grid(row = 7, column = 2) 

# quit button 
btnquit = Button(f1, padx = 16, pady = 8, bd = 16, 
				fg = "black", font = ('arial', 16, 'bold'), 
					width = 10, text = "quit", bg = "red", 
				command = qExit).grid(row = 7, column = 3) 

# keeps window alive 
root.mainloop() 
