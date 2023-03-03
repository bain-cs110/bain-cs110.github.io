try:
    import utilities
    utilities.modify_system_path()
except:
    pass

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_mail(to_emails: list, subject: str, content: str):
    '''
    Uses the SendGrid API to send an email.

    * `to_emails` (`list` or `str`):   [Required] A list of recipient emails, string is fine for one recipient.
    * `subject` (`str`):             [Required] The subject of the email.
    * `content` (`str`):        [Required] Text or HTML to be included in the body of the email.

    Returns `True` if the email was successfully sent, `False` otherwise.
    '''
    message = Mail(
        from_email='nu.compsci110@gmail.com',
        to_emails=to_emails,
        subject=subject,
        html_content=content
    )

    try:
        from apis import my_token
        SENDGRID_TOKEN = my_token.SENDGRID_TOKEN

    except:
        title = 'IMPORTANT: You Need an Access Token!'
        error_message = '\n\n\n' + '*' * len(title) + '\n' + \
            title + '\n' + '*' * len(title) + \
            '\nPlease download the the my_token.py file from Canvas and save it in your apis directory.\n\n'
        raise Exception(error_message)
    
    try:
        sg = SendGridAPIClient(SENDGRID_TOKEN)
        sg.send(message)
        print('Email sent. You may need to check your spam folder.')
        return True
    except Exception as e:
        print(e)
        print("If the above says error 401 or 403, this is not your fault it's Dr. Bain's. See Campuswire for more details.")
        return False