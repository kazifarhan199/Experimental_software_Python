import tkinter as tk
import random

human_score_no=0
computer_score_no=0

def main_handler(first_value):
	global human_score_no,computer_score_no
	x=['stone','paper','scissors']
	second_value=random.choice(x)
	if (first_value=='stone'and second_value=='paper')or(first_value=='paper'and second_value=='scissors')or(first_value=='scissors'and second_value=='stone'):
		computer_score_no+=1
		score_computer.configure(text=computer_score_no)
		main_image_display.configure(image=image_loss)
	elif first_value==second_value:
		main_image_display.configure(image=image_tuy)
	else:
		human_score_no+=1
		score_human.configure(text=human_score_no)
		main_image_display.configure(image=image_win)

def reset():
	global human_score_no,computer_score_no
	human_score_no=0
	computer_score_no=0
	score_computer.configure(text=0)
	score_human.configure(text=0)
	main_image_display.configure(image=image_start)

def Quit(execute='yes'):
	exit()

root=tk.Tk()

image_start=tk.PhotoImage(file='start.png')
image_win=tk.PhotoImage(file='win.png')
image_loss=tk.PhotoImage(file='loos.png')
image_tuy=tk.PhotoImage(file='tuy.png')

image_stone=tk.PhotoImage(file='stone.png')
image_paper=tk.PhotoImage(file='paper.png')
image_scissors=tk.PhotoImage(file='scissors.png')

main_image_display=tk.Label(image=image_start)
main_image_display.grid(row=1,column=1,columnspan=3)

stone_button=tk.Button(text='stone',image=image_stone,command=lambda:main_handler('stone'))
papaer_button=tk.Button(text='papaer',image=image_paper,command=lambda:main_handler('paper'))
scissors_button=tk.Button(text='scissors',image=image_scissors,command=lambda:main_handler('scissors'))
stone_button.grid(row=2,column=1)
papaer_button.grid(row=2,column=2)
scissors_button.grid(row=2,column=3)

score_human_indicator=tk.Label(text="You'r Score",bg='green',width=11)
score_human_indicator.grid(row=3,column=1)
score_vs_indicator=tk.Label(text='vs',bg='gray',width=11)
score_vs_indicator.grid(row=3,column=2)
score_computer_indicator=tk.Label(text="You'r Score",bg='red',width=11)
score_computer_indicator.grid(row=3,column=3)
score_human_indicator.configure(font=(None,13))
score_vs_indicator.configure(font=(None,13))
score_computer_indicator.configure(font=(None,13))

score_human=tk.Label(text=0)
score_human.grid(row=4,column=1)
score_computer=tk.Label(text=0)
score_computer.grid(row=4,column=3)
score_human.configure(font=(None,13))
score_computer.configure(font=(None,13))

reset_button=tk.Button(text='Reset',bg='green',width=34,command=reset)
reset_button.grid(row=5,column=1,columnspan=3)
reset_button.configure(font=(None,'13'))

menu=tk.Menu(root)
root.configure(menu=menu)
file=tk.Menu(menu,tearoff=False)
file.add_command(label='Exit',command=Quit)
menu.add_cascade(label='file',menu=file)

root.bind("<Control-w>",Quit)

root.title('Stone Paper Scissors')
root.iconbitmap('a.ico')
root.resizable(False,False)
root.mainloop()

