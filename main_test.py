import unittest
import main

class Test_main(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(main.hello(), "Hello, World!")

    def test_goodbye_name(self):
        names = ['Daniel', 'Joey', 'Jim-Bob']
        for name in names:
            self.assertEqual(main.goodbye(name), "Goodbye, {}. We'll miss you!".format(name)
        
if __name__ == '__main__':
    unittest.main()
