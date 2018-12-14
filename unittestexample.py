import unittest
from examples import example


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("starting")
    def tearDown(self):
        print("ending")

    def test_add(self):
        result=example.add(self,10,20)
        self.assertEqual(result,30)

    def test_sub(self):
        result=example.sub(self,100,20)
        self.assertEqual(result,80)


#if __name__ == '__main__':
#    unittest.main()
