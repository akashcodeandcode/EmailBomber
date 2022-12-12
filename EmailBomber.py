import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_sender = ""
password = ""
subject = "Hey there!!! I am using Whatsapp"


with open("mail.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)

    for line in reader:
        text = "Hello, " + line[1] + " you are " + line[2]
        # print(text)

        send_email = line[0]
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = send_email
        msg['Subject'] = subject
        msg.attach(MIMEText(text, "plain"))
        text = msg.as_string()

        server = smtplib.SMTP_SSL("smtp.gmail,com", 465)
        server.login(email_sender, password)
        server.sendmail(email_sender, send_email, text)

        server.quit()




