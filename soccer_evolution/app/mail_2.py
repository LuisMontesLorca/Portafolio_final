import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import traceback

def send2(to_list2, email2, password2, hostmail, portmail):
    try:
        subject = "Bienvenido a Soccer Evolution!!!"
        mail_body = ""
        # Read template html
        txt_file = open(os.path.join('templates', 'mail_2.html'))
        mail_body = txt_file.read()
        txt_file.close()
        # Override template html (REPLACE VALUE IN TEMPLATE)
        mail_body = mail_body.replace('#PERSON_NAME', 'John Doe')
        mail_body = mail_body.replace('#DETAIL', 'TESTING DETAIL')
        # Set mail paremeters (SENDMAIL)
        mimemsg = MIMEMultipart()
        mimemsg['From'] = email2
        mimemsg['To'] = to_list2
        mimemsg['Subject'] = subject
        # HTML body
        mimemsg.attach(MIMEText(mail_body, 'html'))
        connection = smtplib.SMTP(host=hostmail, port=portmail)
        connection.starttls()
        connection.login(email2,password2)
        #Send mail
        connection.send_message(mimemsg)
        connection.close()
        print('SENDED MAIL.')
    except Exception as e:
        print('ERROR MAIL.')
        traceback.print_exc()

def send_outlook2(to_list2, email2, password2):
    send2(to_list2, email2, password2, 'm.outlook.com', 587)

def send_gmail2(to_list, email, password):
    send2(to_list, email, password, 'smtp.gmail.com', 465)

