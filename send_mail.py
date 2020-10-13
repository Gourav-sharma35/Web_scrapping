import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_add="deepsharmaGourav@gmail.com"
    to_add="gouravsharma09989@gmail.com"

    subject="finanacial stock report"
    msg=MIMEMultipart()
    msg['From']=from_add
    msg['To']=to_add
    msg['Subject']=subject

    body="<b>Tody financial stock reports</b>"
    msg.attach(MIMEText(body,'html'))

    my_file=open(filename,'rb')

    part=MIMEBase('application','octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition','attachment; filename = ' +  filename )

    msg.attach(part)

    message=msg.as_string()


    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(from_add,'tbzcpanugtuocnxq')
    server.sendmail(from_add,to_add,message)
    server.quit()
