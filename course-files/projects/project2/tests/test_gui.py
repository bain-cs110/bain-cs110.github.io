import unittest
from apis import gui
import helpers
import os
helpers.modify_system_path()

class TestGUI(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestGUI, self).__init__(*args, **kwargs)

    def test_can_import_customtkinter(self, *args, **kwargs):
        from customtkinter import CTk
        self.assertNotEqual(str(CTk).find('CTk'), -1)

if __name__ == '__main__':
    unittest.main()
