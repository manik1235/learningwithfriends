import unittest
import main

class Test_main(unittest.TestCase):
    def test_known_answers(self):
        self.assertEqual(main.hello(), "Hello, World!")