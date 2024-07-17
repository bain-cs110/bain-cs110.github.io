import unittest
import helpers
helpers.modify_system_path()

from tests.test_authentication import TestAuthentication
from tests.test_spotify import TestSpotify
from tests.test_yelp import TestYelp
from tests.test_twilio import TestTwilio
from tests.test_gui import TestGUI


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests([
        TestAuthentication('test_tokens'),
        TestAuthentication('test_get_backup'),
        TestGUI('test_can_import_customtkinter'),
        TestSpotify('test__issue_get_request_only_one'),
        TestYelp('test_execute_business_queries_just_one_simplified'),
        TestTwilio('test_can_import_twilio'),
        TestTwilio('test_can_import_twilio_api_module'),
        TestTwilio('test_can_send_email')
    ])
    unittest.TextTestRunner(verbosity=2).run(suite)
