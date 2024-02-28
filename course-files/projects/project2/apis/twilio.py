try:
    import utilities
    utilities.modify_system_path()
except:
    pass

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

__docformat__ = "google"

def send_email(to_emails: list, subject: str, content: str):
    '''
    Uses the SendGrid (Twilio) API to send an email.

    Args:
        to_emails (`list` or `str`): A list of recipient emails, string is fine for one recipient.
        subject (`str`): The subject of the email.
        content (`str`): Text or HTML to be included in the body of the email.

    Returns:
        a `bool`, specifically `True` if the email was successfully sent, `False` otherwise.
    '''
    message = Mail(
        from_email='nu.compsci110@gmail.com', ## NOTE: Don't modify this or your email won't be sent.
        to_emails=to_emails,
        subject=subject,
        html_content=content
    )

    try:
        from apis import secret_tokens
        SENDGRID_TOKEN = secret_tokens.SENDGRID_TOKEN

    except:
        title = 'IMPORTANT: You Need an Access Token!'
        error_message = '\n\n\n' + '*' * len(title) + '\n' + \
            title + '\n' + '*' * len(title) + \
            '\nPlease download the the secret_tokens.py file from Canvas and save it in your apis directory.\n\n'
        raise Exception(error_message)
    
    try:
        sg = SendGridAPIClient(SENDGRID_TOKEN)
        sg.send(message)
        return True
    except Exception as e:
        print(e)
        print("If the above says error 401 or 403 but does NOT say something about a SSL_CERTIFICATE, this is not your fault it's Dr. Bain's. Post a private post on edSTEM.")
        return False