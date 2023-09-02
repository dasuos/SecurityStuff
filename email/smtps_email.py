from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils as utils
from smtplib import SMTP
from sys import argv

from_address = argv[1]
to_address = argv[2]
subject = argv[3]
smtp_server = argv[4]

with open('email_template.html', 'r') as template:
    template_content = template.read() \
        .replace('\n', '')

    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_address
    message['To'] = to_address
    message['Date'] = utils.formatdate()
    message['Message-ID'] = utils.make_msgid(domain=from_address.split('@')[1])
    message.attach(MIMEText(template_content, 'html'))

    with SMTP(smtp_server, 25) as smtp:
        smtp.starttls()
        smtp.sendmail(from_address, to_address, message.as_string())
