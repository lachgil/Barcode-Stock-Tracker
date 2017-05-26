import smtplib

sender = ''
receivers = ['','']
#mail server must be open ( i.e use your providers mail server) 
mailserver=""

def send(info):
	str = ' '.join(['%s %s' % (k,v) for k,v in info.iteritems()])
	print str
	message = """From: The Stock Room <stock@example.com>
To: Stock Public Folder <stock@example.com>
Subject: New Stock Update
%s
""" % ( str) 
	print message
	
	try:
	   smtpObj = smtplib.SMTP(mailserver)
	   smtpObj.sendmail(sender, receivers, message)         
	   print "Successfully sent email"
	   print info
	except SMTPException:
	   print "Error: unable to send email"
