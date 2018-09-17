#_*_ coding:utf-8 _*_

import unittest
import HTMLTestRunner
import os
import time

# 定义输出的文件位置和名字
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
HtmlFile = report_path+now+"HTMLtemplate.html"
fp = open(HtmlFile, "wb")
#python3 中，打开本地文件需要用fp = open(filename,'wb'),不要再去用file了；关闭该文件可以用fp.close()
# 用例路径
case_path = os.path.join(os.getcwd())
# 报告存放路径
report_path = os.path.join(os.getcwd(), "test_report")
def testsuite():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover
if __name__=='__main__':
#     suite = unittest.TestLoader().discover("test_baidu_search")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'执行情况')
    runner.run(testsuite())
    fp.close()
    
