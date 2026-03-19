import ssl
VERSION = 2026.1 # add insecure path for windows ssl issue

try:
    import utilities
    utilities.modify_system_path()
except:
    pass

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

__docformat__ = "google"

def send_email(to_emails: list, subject: str, content: str, to_file: bool = False, use_alt_ssl: bool = False, try_insecure: bool = False):
    '''
    Uses the SendGrid (Twilio) API to send an email.

    Args:
        to_emails (`list` or `str`): A list of recipient emails, string is fine for one recipient.
        subject (`str`): The subject of the email.
        content (`str`): Text or HTML to be included in the body of the email.
        to_file (`bool`): ONLY USE THIS IF YOU'RE HAVING TROUBLE SENDING EMAILs. It will write the email
           to an HTML file you can view in your web browser rather than actually send an email.
        use_alt_ssl (`bool`): See Prof. Bain for details. This should NOT be used unless he says to try it!
        try_insecure (`bool`): See Prof. Bain for details. This should NOT be used unless he says to try it!

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
    
    if use_alt_ssl:
        try:
            import pip_system_certs.wrapt_requests
        except ModuleNotFoundError as e:
            raise Exception(f"{str(e)}\nIf Dr. Bain asked you to try using the use_alt_ssl input, make sure to follow the instructions given to install this package!")
    
    elif try_insecure:
        ssl._create_default_https_context = ssl._create_unverified_context
        print("Warning, trying insecure send. Only do this if Prof. Bain specifically told you to!")


    try:
        sg = SendGridAPIClient(SENDGRID_TOKEN)
        sg.send(message)
        return True
    except Exception as e:
        print(e)
        print("If you're on a Mac, please make sure to follow the troubleshooting step under the setup instructions for SSL_CERTIFICATE problems. If you've already done that, post a private post on edSTEM with the printed out error above.")
        return False
    
