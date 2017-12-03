import csv 

def csv_soter(name):
	with open(name) as csvfile:
		readCSV  = csv.reader(csvfile, delimiter=',')
		emails=[]

		for i in readCSV:
			email=i[0]

			emails.append(email)

	return(emails)
