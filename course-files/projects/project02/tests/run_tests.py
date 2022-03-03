import helpers
helpers.modify_system_path()

import unittest
from tests.test_authentication import TestAuthentication
from tests.test_yelp import TestYelp
from tests.test_spotify import TestSpotify


if __name__ == '__main__':
    unittest.main()
