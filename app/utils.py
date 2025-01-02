import re
from flask_mail import Message
from config import Config  # Importing configuration values

class VerificationService:
    def __init__(self, mail):
        self.mail = mail

    def send_verification_email(self, email):
        msg = Message(
            subject='Verification Email',
            sender=Config.EMAIL_SENDER,
            recipients=[email]
        )
        msg.body = 'Please verify your email address by clicking the link below.'
        self.mail.send(msg)
        
def validate_email_format(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None