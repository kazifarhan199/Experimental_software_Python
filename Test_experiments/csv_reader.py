import csv
from datetime import date
import datetime

Date=[]
name=[]
transition=[]
amount=[]


def csv_reader():
	global Date,name,transition,amount
	with open('b.csv') as csvfile:
		readCSV  = csv.reader(csvfile, delimiter='|')
		dates=[]
		names=[]
		transitions=[]
		amounts=[]

		for i in readCSV:

			dates = i[0]
			names = i[1]
			transitions=i[2]
			amounts = i[3]

			Date.append(dates)
			name.append(names)
			transition.append(transitions)
			amount.append(amounts)	

	return 	Date,name[::-1],transition[::-1],amount[::-1]

def csv_appender(new_transition_name,new_transition_ammount):
	amount=[]
	with open('b.csv') as csvfile:
		readCSV  = csv.reader(csvfile, delimiter='|')
		
		amounts=[]

		for i in readCSV:
			amounts = i[3]
			amount.append(amounts)	

	csv_appending_file=open('b.csv','a')
	csv_appending_file.write(str(datetime.date.today())+'|'+str(new_transition_name)+'|'+str(new_transition_ammount)+'|'+str(int(new_transition_ammount)+int(amount[-1]))+'\n')

def csv_writer(new_Date,new_name,new_transition,new_amount,element_no):
	new_csv=open('b.csv','w')
	new_csv.write('')
	new_csv.close()

	new_csv_writer=open('b.csv','a')
	for i in range(len(new_Date)):
		new_csv_writer.write(str(new_Date[i])+'|'+str(new_name[i])+'|'+str(new_transition[i])+'|'+str(new_amount[i])+'\n')
	new_csv_writer.close()

#writer(['new_Date','new_amount'],['new_name','new_amount'],['new_transition','new_amount'],['new_amount','new_amount'],0)