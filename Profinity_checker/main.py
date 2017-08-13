import urllib
from urllib import request
from tkinter import *
from tkinter import filedialog
import re

def Quit(event='true'):
	exit()

def file_importer():
	global text_box
	results=filedialog.askopenfilename(filetypes=((''
		,'*.txt'),('Allfiles','*.*')))
	text_box.delete('1.0', END)
	text_box.insert('1.0',results)
	try:
		file=open(results)
		key_word_holder=file.read()
		search_engion(key_word_holder)
	except:
		pass
	
def search_engion(key_word_holder):
	headers={}
	key_word_holder=re.sub(r"\s+", '+', key_word_holder)
	headers['User-Agent'] =  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
	resp=urllib.request.Request("http://www.wdylike.appspot.com/?q="+key_word_holder,headers=headers)
	apple=urllib.request.urlopen(resp)
	a=apple.read()
	
	if a==b'true':
		found=Label(text='     Found Profanity        ',font=(None,13),fg='red')
		found.grid(row=10,column=1)
	else:
		not_found=Label(text='No Profanity Found',font=(None,13),fg='green')
		not_found.grid(row=10,column=1)

root=Tk()
text_box=Text(width=30,height=11)
text_box.grid(row=1,column=1,rowspan=4)
find_error=Button(command=lambda:search_engion(text_box.get("1.0",END)),text='Scarch Profanity',font=(None,10),width=13,height=5)
find_error.grid(row=1,column=2,rowspan=2)
fiel_taker=Button(text='Import a file',command=file_importer,font=(None,10),width=13,height=5)
fiel_taker.grid(row=3,column=2,rowspan=2)
root.iconbitmap('a.ico')
root.mainloop()