import unittest
import helpers
helpers.modify_system_path()

from tests.test_authentication import TestAuthentication
from tests.test_twilio import TestTwilio
from tests.test_gui import TestGUI


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests([
        TestAuthentication('test_tokens'),
        TestGUI('test_can_import_customtkinter'),
        TestTwilio('test_can_import_twilio'),
        TestTwilio('test_can_import_twilio_api_module'),
        TestTwilio('test_can_send_email')
    ])
    unittest.TextTestRunner(verbosity=2).run(suite)
