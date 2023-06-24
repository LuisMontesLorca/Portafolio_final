import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import traceback

def send3(to_list3, email3, password3, hostmail, portmail):
    try:
        subject = "Bienvenido a Soccer Evolution!!!"
        mail_body = ""
        # Read template html
        txt_file = open(os.path.join('templates', 'mail_3.html'))
        mail_body = txt_file.read()
        txt_file.close()
        # Override template html (REPLACE VALUE IN TEMPLATE)
        mail_body = mail_body.replace('#PERSON_NAME', to_list3)
        mail_body = mail_body.replace('#DETAIL', 'TESTING DETAIL')
        mail_body = mail_body.replace('{{ url_for(\'cambio_contrasena\') }}', 'http://127.0.0.1:5000/cambio_contrasena')
  # Reemplaza con la URL correcta
        # Set mail paremeters (SENDMAIL)
        mimemsg = MIMEMultipart()
        mimemsg['From'] = email3
        mimemsg['To'] = to_list3
        mimemsg['Subject'] = subject
        # HTML body
        mimemsg.attach(MIMEText(mail_body, 'html'))
        connection = smtplib.SMTP(host=hostmail, port=portmail)
        connection.starttls()
        connection.login(email3,password3)
        #Send mail
        connection.send_message(mimemsg)
        connection.close()
        print('SENDED MAIL.')
    except Exception as e:
        print('ERROR MAIL.')
        traceback.print_exc()

def send_outlook3(to_list3, email3, password3):
    send3(to_list3, email3, password3, 'm.outlook.com', 587)

def send_gmail3(to_list3, email3, password3):
    send3(to_list3, email3, password3, 'smtp.gmail.com', 465)

