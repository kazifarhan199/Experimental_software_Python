import tkinter as tk
import webbrowser



def open_link(text_provided):
	chrome_path="C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"
	webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),0)

	main_lib={
	'cleaverprogrammer':'http://cleverprogrammer.teachable.com'
	,'shopify':'https://www.shopify.com/login'
	,'udacity':'https://in.udacity.com/'
	,'youtube':'https://www.youtube.com/user/sentdex'
	,'programmersstuff':'programmersstuff.com'
	,'zoho':'https://mail.zoho.com/zm/#mail/folder/inbox'
	,'godaddy':'godaddy.com'
	,'githun':'https://github.com'
	}

	webbrowser.get('chrome').open_new(main_lib[text_provided])

#####################################################################

def Buttons_1(text_provided,image_one,y,bg,fg='black'):
	tk.Label(image=image_one,width=220,height=240).grid(row=1,column=y)
	tk.Button(text=text_provided,command=lambda:open_link(text_provided),fg=fg,width=20,font=(None, 15),bg=bg).grid(row=2,column=y)

##################################################################

root=tk.Tk()
root.resizable(False, False)
root.bind('<Control-w>',exit)

###################################################################

image_cleaverprogrammer=tk.PhotoImage(file='cleaverprogrammer.png')
image_zoho=tk.PhotoImage(file='zoho.png')
image_godaddy=tk.PhotoImage(file='godaddy.png')
image_shopify=tk.PhotoImage(file='shopify.png')
image_udacity=tk.PhotoImage(file='udacity.png')
image_youtube=tk.PhotoImage(file='youtube.png')
image_github=tk.PhotoImage(file='github.png')
image_programmersstuff=tk.PhotoImage(file='programmersstuff.png')

###################################################################

Buttons_1(text_provided='cleaverprogrammer',image_one=image_cleaverprogrammer,y=0,bg='dark orange')
Buttons_1(text_provided='udacity',image_one=image_udacity,y=1,bg='DodgerBlue2')
Buttons_1(text_provided='youtube',image_one=image_youtube,y=2,bg='red3')
Buttons_1(text_provided='github',image_one=image_github,y=3,bg='black',fg="white")

##############################################################################

def Buttons_2(text_provided,image_one,y,bg):
	tk.Label(image=image_one,width=220,height=240).grid(row=3,column=y)
	tk.Button(text=text_provided,command=lambda:open_link(text_provided),width=20,font=(None, 15),bg=bg).grid(row=4,column=y)

##########################################################################
Buttons_2(text_provided='programmersstuff',image_one=image_programmersstuff,y=0,bg='turquoise1')
Buttons_2(text_provided='zoho',image_one=image_zoho,y=1,bg='blue')
Buttons_2(text_provided='godaddy',image_one=image_godaddy,y=2,bg='lime green')
Buttons_2(text_provided='shopify',image_one=image_shopify,y=3,bg='green3')

root.iconbitmap('apple.ico')
root.mainloop()
