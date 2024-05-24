import time
from apis import authentication
import unittest
import helpers
helpers.modify_system_path()

class TestAuthentication(unittest.TestCase):

    def test_tokens(self):

        try:
            from apis import secret_tokens
                
            self.assertEqual(len(secret_tokens.API_TUTOR_TOKEN),
                            40)
            self.assertEqual(len(secret_tokens.SENDGRID_TOKEN),
                            69)
            self.assertEqual(len(secret_tokens.SPOTIFY_CLIENT_ID),
                            32)
            self.assertEqual(len(secret_tokens.SPOTIFY_CLIENT_SECRET),
                            32)
            self.assertEqual(len(secret_tokens.YELP_API_TOKEN),
                            128)
        
        except:
            title = 'IMPORTANT: You Need an Access Token!'
            error_message = '\n\n\n' + '*' * len(title) + '\n' + \
                title + '\n' + '*' * len(title) + \
                '\nPlease download the the secret_tokens.py file from Canvas and save it in your apis directory.\n\n'
            raise Exception(error_message)

    def test_get_backup(self):
        yelp_key = authentication.get_token(
            'https://www.apitutor.org/yelp/key')
        
        time.sleep(1.0)
        
        spotify_key = authentication.get_token(
            'https://www.apitutor.org/spotify/key')
        
        self.assertEqual(len(yelp_key) != 0, True)
        self.assertEqual(len(spotify_key) != 0, True)


if __name__ == '__main__':
    unittest.main()
