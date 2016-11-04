# Geschreven door Robin


import smtplib
import re
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


class SendEmail:
	"regex email matching patern"
	_regexPatern = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
	_fromEmail = "Kaas@kaas.nl"
	_toEmail = []
	_emailBody = ""
	_emailMessage = ""
	_emailSubject = ""


	def SetMessage(self, message):
		"Zet het email bericht"
		self._emailMessage = message


	def SetSubject(self,subject):
		"Zet het email subject"
		self._emailSubject = subject


	def BuildEmailToString(self,emailArray):
		"Join the emails naar een string"
		return ",".join(emailArray)


	def Send(self,fileLocations = None):
		"Verzend de email"

		if(len(self._toEmail) <= 0):
			return False

		try:
			msg = MIMEMultipart()
			msg['From'] = self._fromEmail
			msg['To'] = COMMASPACE.join(self._toEmail)
			msg['Subject'] = self._emailSubject
			if fileLocations:
				f = open(fileLocations)
				attachment = MIMEText(f.read())
				attachment.add_header('Content-Disposition', 'attachment', filename=fileLocations)
				msg.attach(attachment)

			smtp = smtplib.SMTP('localhost')
			smtp.sendmail(self._fromEmail, self._toEmail, msg.as_string())
			smtp.close()
			return True

		except Exception as ex:
			print("Error:",str(ex))

		return False


	def AppendEmail(self, emailAddress):
		"voegt een email address toe"
		if not self.IsValidEmail(emailAddress):
			return False

		self._toEmail.append(emailAddress)

		return True


	def IsValidEmail(self,emailAddress):
		"Valideerd het email address"
		return re.search(self._regexPatern, emailAddress, flags=0)
