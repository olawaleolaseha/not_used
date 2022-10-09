#sending email with python without logging into the email client.
#for example, app password will be created from gmail account and be used in the code (or app) that is being written below.
# an attacker use case is the attacker needs to only compromise your gmail password once and go inside to create this app password that he can 
# #now use anytime to send email from your gmail without physically logging into your gmail anymore. This could be used in BEC. So it is important to protect your
# gmail user/interactive password.
# Note that the app password mentioned above is like system password. The app or code applies it behind the scene, unlike an interactive user password.

from email.message import EmailMessage
from optparse import AmbiguousOptionError
import ssl
import smtplib

msg = input("Enter your message: ")
recipient = input("Enter recipient's email address: ")

sender_email = "olawale.olaseha@gmail.com"
sender_password = 'usaijzuhfutgetwz' #generate a new app password and update this password when next you run this code. I have deleted 
                                    #this "specific application password" from my gmail account.
receiver_email = recipient

subject = input("Enter the Subject of the email: ")
body = msg

em = EmailMessage()
em['From'] = sender_email
em['To'] = receiver_email
em['Subject'] = subject
em.set_content(body)

#there is either a bug in the above code, or gmail security is preventing it to work. investigate with other programmers

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, receiver_email, em.as_string())