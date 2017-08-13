import urllib
from urllib import request
import re 
from tkinter import *

def Quit(event='true'):
	exit()

def inserts(results):
	result_text=Text(width=46,height=20)
	result_text.grid(row=2,column=1,columnspan=2)
	results.reverse()
	for i in results:
		result_text.insert(1.0,'\n')
		result_text.insert(1.0,i)
		result_text.insert(1.0,'______________________________________________\n')
	

def search_engion(key_word_holder='true'):
	key_word_holder=key_word.get()
	headers={}
	key_word_holder=re.sub(r"\s+", '+', key_word_holder)
	print(key_word_holder)
	headers['User-Agent'] =  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
	resp=urllib.request.Request("https://www.google.co.in/search?q="+key_word_holder,headers=headers)
	apple=urllib.request.urlopen(resp)
	a=apple.read()
	paragrphs = re.findall(r'<cite class="_Rm">(.*?)</cite>',str(a))   
	list_of_sites=[]
	for i in paragrphs: 
		list_of_sites.append(i)
	inserts(list_of_sites)
	

root=Tk()
image_search=PhotoImage(file='a.png')
search=Button(image=image_search,text='Search',
	fg='white',font=(None,15),command=search_engion)
search.grid(row=1,column=2)
key_word=Entry(width=43)
key_word.grid(row=1,column=1)
key_word.focus()
root.iconbitmap('a.ico')
root.bind("<Return>",search_engion)
root.bind("<Control-w>",Quit)
root.mainloop()