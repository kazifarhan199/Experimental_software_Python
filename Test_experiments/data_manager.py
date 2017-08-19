import csv

def csv_reader():
	csv_file=open('csv_file.csv','r')
	csv_file_read=csv.reader(csv_file,delimiter='|')

	date_of_transition=[]
	name_of_transition=[]
	amount_of_transition=[]
	amount_of_balance=[]

	date_of_transition_containor=[]
	name_of_transition_containor=[]
	amount_of_transition_containor=[]
	balance_containor=0

	for no_of_line in csv_file_read:

		date_of_transition_containor=no_of_line[0]		
		name_of_transition_containor=no_of_line[1]		
		amount_of_transition_containor=no_of_line[2]
		
		date_of_transition.append(date_of_transition_containor)
		name_of_transition.append(name_of_transition_containor)
		amount_of_transition.append(amount_of_transition_containor)

		balance_containor+=int(amount_of_transition_containor)

		amount_of_balance.append(balance_containor)

	return date_of_transition, name_of_transition, amount_of_transition, amount_of_balance

def csv_append( date, transition_name, transition_ammount):
	csv_file=open('csv_file.csv','a')
	data_to_append=str(date)+'|'+str(transition_name)+'|'+str(transition_ammount)+'\n'
	csv_file.write(data_to_append)
	csv_file.close()
	return csv_reader()

def csv_write(new_dates, new_transition_names, new_transition_ammount):
	csv_file=open('csv_file.csv','w')
	csv_file.write('')
	csv_file.close()
	csv_file=open('csv_file.csv','a')

	for i in range(len(new_dates)):
		csv_file.write(str(new_dates[i])+'|'+str(new_transition_names[i])+'|'+str(new_transition_ammount[i])+'\n')

	csv_file.close()
	return csv_reader()
