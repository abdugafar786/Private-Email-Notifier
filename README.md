# Private Email Notifier

This project has been developed to check your email inbox.I do not check my emails frequently because I sometimes receive unnecessary emails. 
However, since I have sent CV to some workplaces,I want to ensure that the important ones reach me. Therefore, I want to check the emails coming from specific senders to see which emails have arrived.

## Features
- Connects to IMAP email server
- Checks for unseen emails
- Filters emails from specific senders
- Monitors emails from specified senders
- Sends desktop notifications for important emails


## Requirements
- Python 3.11.6
- imaplib
- email
- notify-py

### Before starting the project, please create the .env file and add this code
```env
EMAIL_ADDRESS=your_email@example.com
APP_PASSWORD=your_app_password


