# Sending e-mails with Python

In all examples I am using a gmail server to send emails. If you are not using a gmail address you need to insert the respective smtp server and possibly the port.

- Gmail: smtp.gmail.com, port 587
- Hotmail: smtp.live.com, port 587
- Outlook: smtp-mail.outlook.com, port 587


### Very basic example
This is a very barebones example. No subject is added to the email. 

```python
import smtplib

sender = 'sender@gmail.com'
pwd = 'senderpassword'  # password for sender email
receiver = 'receiver@gmail.com'
msg = 'Hi there!'

server = smtplib.SMTP('smtp.gmail.com', 587)  # smtp server and port for the sender email
server.ehlo()
server.starttls()  # starts a TLS encrypted connection
server.login(sender, pwd)
server.sendmail(sender, receiver, msg)
server.close()

print('Mail sent!')
```

---

### More complete case
This uses the Python email library to help compose the email. You can add the subject to the email. 

```python
import smtplib
from email.message import EmailMessage

sender = 'sender@gmail.com'
pwd = 'senderpassword'  # password for sender email
receiver = 'receiver@gmail.com'
message = 'Hi there!'

msg = EmailMessage()
msg.set_content(message)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()  # starts a TLS encrypted connection
server.login(sender, pwd)
server.sendmail(sender, receiver, msg.as_string())
server.close()

print('Mail sent!')
```
