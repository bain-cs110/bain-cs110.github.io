import requests
API_TUTOR_TOKEN = None
try:
    import utilities
    utilities.modify_system_path()
except:
    pass

def get_token(url):
    '''
    Retrieves the authentication token for the particular provider.

    * url (str): Required. The endpoint to the platform's token on API Tutor.  
    
    Returns the authentication token.
    '''
    response = requests.get(url + '?auth_manager_token=' + API_TUTOR_TOKEN)
    data = response.json()
    return data['token']