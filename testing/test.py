import unittest
from main import do_stuff

class TestMain(unittest.TestCase):
    def setup(self):
        print('about to test a function')
    def test_do_stuff(self):
        '''HIIIIIIII'''
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shkshks'
        result = do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff5(self):
        test_param = 0
        result = do_stuff(test_param)
        self.assertEqual(result, 5)
    
    def tearDown(self):
        print('cleaning up')
if __name__ == '__main__':
    unittest.main()