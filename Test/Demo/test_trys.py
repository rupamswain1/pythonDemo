
from builtins import classmethod
import unittest
import HtmlTestRunner
class trya(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("will run start for every class")

    def setUp(self):
        print("will run before every test Run")

    def tearDown(self):
        print("will run after every test method")

    def test_one(self):
        print("test1")
        assert 5==5

    def test_two(self):
        print("test2")
        assert 2==2

    @classmethod
    def tearDownClass(cls):
        print("will run for at class end")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="F://Python_Worksapce//PythonBasics//Reports"))