import imaplib
import email
from dotenv import load_dotenv
import os
from notifypy import Notify


load_dotenv()

email_address = os.getenv('EMAIL_ADDRESS')
app_password = os.getenv('APP_PASSWORD')


def control_email(email_address: str, app_password: str) -> None:
    try:
        mail = imaplib.IMAP4_SSL('imap.mail.me.com')
        mail.login(email_address, app_password)
        mail.select('inbox')
        notification = Notify()

        status, messages = mail.search(None, 'UNSEEN')

        if status != 'OK':
            print("An error occurred during the search.")
            return

        if messages[0] == b'':
            print("There are no messages from companies")
            return

        mail_ids = messages[0].split() 
        
        for mail_id in mail_ids:
            status, msg_data = mail.fetch(mail_id, "(BODY.PEEK[HEADER])")
            if status == 'OK':
                msg = email.message_from_bytes(msg_data[0][1]) 
                if msg['from'] in ['info@zet-mobile.com', 'info@tcell.tj', 'info@megafon.tj'] :
                    notification.title = f'New Email from: {msg["from"]}'
                    notification.send()
                    print(f"incoming email: {msg['from']}")
            else:
                print("An error occurred while retrieving email.")

    except Exception as e:
        print(f"Eror: {e}")
        
    finally:
        
        mail.logout()

control_email(email_address, app_password)
