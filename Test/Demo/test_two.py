
import unittest
import HtmlTestRunner
class testTwo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("second test started")

    @classmethod
    def tearDownClass(cls):
        print("Second Test ended")

    def test_noOne(self):
        print("one")
        assert 1==1

    def test_two(self):
        print("two")
        assert 2==2

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="F://Python_Worksapce//PythonBasics//Reports"))