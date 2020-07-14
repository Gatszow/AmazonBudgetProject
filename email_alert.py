import config
import smtplib


class EmailAlert(object):
    def __init__(self, subject, msg):
        self.subject = subject
        self.msg = msg

    def send_email(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.FROM_EMAIL_ADDRESS, config.PASSWORD)
            message = f'Subject: {self.subject}\n\n{self.msg}'
            server.sendmail(config.FROM_EMAIL_ADDRESS, config.TO_EMAIL_ADDRESS, message)
            print('Success: Email sent!')
        except smtplib.SMTPException:
            print('Email failed to send.')
