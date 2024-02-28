import requests
API_TUTOR_TOKEN = None
try:
    import utilities
    utilities.modify_system_path()
except:
    pass

def set_main_apitutor_token():
    '''Checks to make sure that you have included the API Tutor token in the secret_tokens.py file.'''
    global API_TUTOR_TOKEN
    try:
        from apis import secret_tokens
        API_TUTOR_TOKEN = secret_tokens.API_TUTOR_TOKEN
    except:
        title = 'IMPORTANT: You Need an Access Token!'
        error_message = '\n\n\n' + '*' * len(title) + '\n' + \
            title + '\n' + '*' * len(title) + \
            '\nPlease download the the secret_tokens.py file from Canvas and save it in your apis directory.\n\n'
        raise Exception(error_message)
    
set_main_apitutor_token()


def get_token(url):
    '''
    Retrieves the authentication token for the particular provider.

    * url (str): Required. The endpoint to the platform's token on API Tutor.  
    
    Returns the authentication token.
    '''
    response = requests.get(url + '?auth_manager_token=' + API_TUTOR_TOKEN)
    data = response.json()
    return data['token']