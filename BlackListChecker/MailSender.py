import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr


class Act:
    _Data = {
        "port" : 465,
        "pwd" :  SENDERPWD,
        "sender_email": SENDER,
    }
    _Context = ssl.create_default_context()
    
    def Send(text, subject, sender_name, receiver_email):
        try:
            
            message = EmailMessage()
            message['Subject'] = subject
            message['From'] = formataddr((sender_name, Act._Data['sender_email']))
            message['To'] = receiver_email
            message.set_content(text)
            
            with smtplib.SMTP_SSL("smtp.gmail.com", Act._Data['port'], context= Act._Context) as server:
                server.login(Act._Data['sender_email'], Act._Data['pwd'])
                server.send_message(message)
                
            return (True, "200")
        except Exception as ex:
            return (False, ex)