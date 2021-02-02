import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()
api_key = os.getenv('SENDGRID_KEY')
sender = os.getenv('SG_FROM')
receiver = os.getenv('SG_TO')


def sendConfirmation(isClockingIn):
    subjectLine = 'Clocked In' if isClockingIn else 'Clocked Out'
    message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject=subjectLine,
        html_content='<strong>Clock Event Confirmed</strong'
    )

    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e.message)


def sendError():
    message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject="Error Clocking",
        html_content='<strong>Likely need to change your password</strong>'
    )
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e.message)
