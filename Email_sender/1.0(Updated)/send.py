def main(from_the_person,passward,email_to,subject_of_mail,Email_message):
	import smtplib
	this_is_exceptiion_indicator=0	

	emails=email_to

	try:
		mail=smtplib.SMTP('smtp.gmail.com',587)

		mail.ehlo()
		mail.starttls()
		mail.ehlo()

	except Exception as e:
		import Sender_show
		this_is_exceptiion_indicator=1
		Sender_show.internet_problem()
		print(1)

	if this_is_exceptiion_indicator==0:
		try:
			my_email=from_the_person
			passa=passward
			mail.login(from_the_person,passward)
		except Exception as e:
			import error_handeller
			this_is_exceptiion_indicator=2
			error_handler.login_error()
			print(2)

	if this_is_exceptiion_indicator==0:
		try:
			subjec=subject_of_mail
			text=str(Email_message)
			message = 'Subject: {}\n\n{}'.format(subjec, text)
			if type(emails)==str:
				mail.sendmail(my_email,emails,message)
				
			elif type(emails)==list:
				for i in emails:
					mail.sendmail(my_email,i,message)	

		except Exception as e:
			import Sender_show
			this_is_exceptiion_indicator=3		
			Sender_show.file_problem_or_unknown_problem()
			print(3)
		mail.close()

if __name__ == '__main__':
	main('youremailadress','passward','to_Whome_his_email',
		'Subject','Message')
