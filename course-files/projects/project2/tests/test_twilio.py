import unittest
from apis import twilio
import helpers
import os
helpers.modify_system_path()

class TestTwilio(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestTwilio, self).__init__(*args, **kwargs)

    def test_can_import_twilio(self, *args, **kwargs):
        from sendgrid.helpers.mail import Mail
        self.assertNotEqual(str(Mail).find('Mail'), -1)

    def test_can_import_twilio_api_module(self, *args, **kwargs):
        self.assertNotEqual(
            str(twilio.send_email).find('function send_email'), -1)

    def test_can_send_email(self, *args, **kwargs):
        email_address = input("Please enter your email address: ")
        self.assertTrue(twilio.send_email(
                email_address,
                f"[CS 110] {os.getlogin()} Test Successful",
                "Twilio Test Successful.")
                )


if __name__ == '__main__':
    unittest.main()
