import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import traceback

def send2(to_list2, email2, password2, hostmail, portmail, transaccion):
    try:
        transaccion=str(transaccion)
        print ("datos en el envio del correo: " +transaccion)
        subject = "Arriendo completado satisfactoriamente!!!"
        mail_body = ""
        # Read template html
        txt_file = open(os.path.join('templates', 'mail_2.html'))
        mail_body = txt_file.read()
        txt_file.close()
        # Override template html (REPLACE VALUE IN TEMPLATE)
        mail_body = mail_body.replace('#PERSON_NAME', 'John Doe')
        mail_body = mail_body.replace('#DETAIL', 'TESTING DETAIL')
        mail_body = mail_body.replace('#TRANSACCION', str(transaccion))

        # Set mail paremeters (SENDMAIL)
        mimemsg = MIMEMultipart()
        mimemsg['From'] = email2
        mimemsg['To'] = to_list2
        mimemsg['Subject'] = subject
        # HTML body
        mimemsg.attach(MIMEText(mail_body, 'html'))
        connection = smtplib.SMTP(str(hostmail), port=int(portmail))
        connection.starttls()
        connection.login(email2,password2)
        #Send mail
        connection.send_message(mimemsg)
        connection.close()
        print('SENDED MAIL.')
    except Exception as e:
        print('ERROR MAIL.')
        traceback.print_exc()

def send_outlook2(to_list2, email2, password2,transaccion):
    send2(to_list2, email2, password2,'m.outlook.com', 587,transaccion)

def send_gmail2(to_list2, email2, password2,transaccion):
    send2(to_list2, email2, password2,'smtp.gmail.com', 465,transaccion)

