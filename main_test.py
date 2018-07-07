import unittest
import main

class Test_main(unittest.TestCase):
    def test_known_answers(self):
        self.assertEqual(main.hello(), "Hello, World!")
        
if __name__ == '__main__':
    unittest.main()