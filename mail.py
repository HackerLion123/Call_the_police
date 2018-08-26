import smtplib
import os
from email.mime.multipart import MIMEMultipart   
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 

def send_mail(crime,proof1,proof2):
	fromaddr = "crimealerte@gmail.com"
	toaddr = "siddharth.dicaprio@gmail.com"
	 
	msg = MIMEMultipart()
	 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Emergency"
	body = crime
	msg.attach(MIMEText(body, 'plain'))
	filename = [proof1,proof2]
	for i in range(len(filename)) :
	    attachment = open(os.path.join(os.getcwd(),filename[i]), "rb")
	    part = MIMEBase('application', 'octet-stream')
	    part.set_payload((attachment).read())
	    encoders.encode_base64(part)
	    part.add_header('Content-Disposition', "attachment; filename= %s" % filename[i])
	    msg.attach(part)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "googleaccount")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
