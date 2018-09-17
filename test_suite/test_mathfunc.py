import unittest
from .mathfunc import *
import HTMLTestRunner
class TestMathFunc(unittest.TestCase):

    def test_01(self):
        self.assertEqual(3,add(1,4))
    def test_02(self):
        self.assertEqual(5,add(1,4))

if __name__ == '__main__':
    filepath = '../report/htmlreport.html'
    ftp=open(filepath,'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMathFunc('test_01'))
    suite.addTest(TestMathFunc('test_02'))
    runner=HTMLTestRunner.HTMLTestRunner(stream=ftp,title='welcome to this web')
    runner.run(suite)
    unittest.main()
