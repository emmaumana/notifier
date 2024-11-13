import os
import ssl
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
from value_objects.support_request import SupportRequestEmailValueObject

load_dotenv()

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
EMAIL_PROVIDER = os.getenv('EMAIL_ADDRESS')
EMAIL_PROVIDER_PASSWORD = os.getenv('EMAIL_PASSWORD')

def send_email(params: SupportRequestEmailValueObject):
    """
    Envía un correo electrónico utilizando SMTP con conexión SSL.
    """
    if not EMAIL_PROVIDER or not EMAIL_PROVIDER_PASSWORD:
        return False, "Missing email credentials."

    msg = create_email_message(params)
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as smtp:
            smtp.login(EMAIL_PROVIDER, EMAIL_PROVIDER_PASSWORD)
            smtp.send_message(msg)
            return True, "Email sent successfully."
    except smtplib.SMTPAuthenticationError:
       return False, "Authentication error: verify your credentials."
    except smtplib.SMTPConnectError:
       return False, "Could not establish connection to the server."
    except Exception as e:
       return False, f"Email sending error: {e}"


def create_email_message(params: SupportRequestEmailValueObject) -> EmailMessage:
    """
    Crea el mensaje con los parámetros proporcionados.
    """
    msg = EmailMessage()
    msg['From'] = EMAIL_PROVIDER
    msg['To'] = params.receiver
    msg['Subject'] = f'[Support Team]: response to your request regarding {params.topic}'
    msg.set_content(params.message)
    return msg