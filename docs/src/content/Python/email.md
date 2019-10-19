Title: Sending e-mails with Python
Date: 2017-08-04 11:12
Authors: José Aniceto


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

---

### HTML email
Here’s an example of how to create an HTML message with an alternative plain text version.

```python
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "my@email.com"
you = "your@email.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
s = smtplib.SMTP('localhost')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
```
