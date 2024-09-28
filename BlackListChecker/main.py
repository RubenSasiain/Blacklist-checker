from time import sleep

import APICall
import MailSender

if __name__ == "__main__":
    while True:
        
        blacklisted = APICall.Request.Listed_request()
        reported = False
        
        if blacklisted[0]:
            subject = "Blacklisted"
            is_active = str(blacklisted[1]['is_active'])
            warnings = str(blacklisted[1]['warnings'])
            summary = str(blacklisted[1]['status_summary'])
            address = str(blacklisted[1]['address'])
            receiver_email = RECEIVER
            message = f"""\
                Address:        {address}
                Is active:      {is_active}
                Warnings:       {warnings}
                Status summary: {summary}
            """
            
            if(not reported):
                mail_response = MailSender.Act.Send(text=message, subject=subject, sender_name="BlackList checker", receiver_email=receiver_email)
                reported = mail_response[0]
                
                if not mail_response[0]: 
                    print(mail_response[1])
        sleep(3600)