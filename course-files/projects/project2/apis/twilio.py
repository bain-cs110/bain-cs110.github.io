try:
    import utilities
    utilities.modify_system_path()
except:
    pass

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

__docformat__ = "google"

def send_email(to_emails: list, subject: str, content: str, to_file: bool = False):
    '''
    Uses the SendGrid (Twilio) API to send an email.

    Args:
        to_emails (`list` or `str`): A list of recipient emails, string is fine for one recipient.
        subject (`str`): The subject of the email.
        content (`str`): Text or HTML to be included in the body of the email.
        to_file (`str`): ONLY USE THIS IF YOU'RE HAVING TROUBLE SENDING EMAILs. It will write the email
           to an HTML file you can view in your web browser rather than actully send an email.

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
    
    if to_file:
        print("DEBUG: Writing email to file as requested.")
        out_file = open("email_output.html","w") 
        out_file.write("<html>\n<head>\n<title>Email Output</title>\n</head>")
        out_file.write(f"<p><b>SUBJECT:</b>{subject}</p>")
        out_file.write(f"<p><b>TO:</b>{to_emails}</p>")
        out_file.write(content)
        out_file.write("</html>")
        out_file.close()

    
    try:
        sg = SendGridAPIClient(SENDGRID_TOKEN)
        sg.send(message)
        return True
    except Exception as e:
        print(e)
        print("If you're on a Mac, please make sure to follow the trouble shooting step under the setup instructions for SSL_CERTIFICATE problems. If you've already done that,  post a private post on edSTEM with the printed out error above.")
        return False
    
