from tkinter import *

def send_complete():
	master=Tk()
	provided_email_error_label=Label(master,bg='green',
		text="Sending sucessful")
	provided_email_error_label.config(font=("",20))
	master.mainloop()
