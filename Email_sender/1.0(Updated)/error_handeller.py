from tkinter import *

def internet_error():
	master=Tk()
	internet_error_label=Label(master,bg='red',
		text="Check you'r internet connection")
	internet_error_label.config(font=("",20))
	internet_error_label.pack()
	master.mainloop()

def login_error():
	master=Tk()
	login_error_label=Label(master,bg='red',
		text="Check you'r e-mail or passward")
	login_error_label.config(font=("",20))
	login_error_label.pack()
	master.mainloop()

def provided_email_error():
	master=Tk()
	provided_email_error_label=Label(master,bg='red',
		text="E-mail to send dos not exist")
	provided_email_error_label.config(font=("",20))
	master.mainloop()
