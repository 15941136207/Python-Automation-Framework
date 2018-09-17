import unittest
import time
import os
import smtplib
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def new_report(report_dir):
    '''
    :param report_dir:报告路径
    :return:返回最新的文件
    '''
    #获取路径下的文件
    lists = os.listdir(report_dir)
    #按照时间顺序排序
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + fn))
    #获取最近时间的
    new_report = os.path.join(report_dir,lists[-1])
    return new_report



def send_mail(new_report,new_report_fail,now):
    '''
    :param new_report:获取最新的文件
    :param new_report_fail:获取最新的文件的路径
    :param now:当前生成报告的时间
    :return:
    '''

    senduser = 'xxx@126.com'
    sendpswd = 'xxx'
    receuser = 'xxx@xxx.com.cn'

    #获取报告文件：'related'43行
    f = open(new_report,'rb')
    body_main = f.read()

    msg = MIMEMultipart()
    # 邮件标题
    msg['Subject'] = Header('TCS系统自动化测试报告','utf-8')
    msg['From'] = senduser
    msg['To'] = receuser
    #邮件内容
    text = MIMEText(body_main,'html','utf-8')
    msg.attach(text)

    #发送附件
    att = MIMEApplication(open(new_report_fail, 'rb').read())
    # att = MIMEText(sendfile, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '',now + "_report.html"))
    msg.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login(senduser,sendpswd)
    smtp.sendmail(senduser,receuser,msg.as_string())


if __name__ == '__main__':
    startime = time.strftime('%H:%M:%S')
    print("开始时间为：%s" % startime)
    #测试路径
    test_dir = './tcs/test_case'
    #报告路径
    report_dir = './tcs/report/'

    now = time.strftime('%Y-%m-%d_%H-%M-%S')
    # 创建完整报告文件
    new_report_fail = report_dir + now + '_result.html'
    fp = open(new_report_fail,'wb')

    runner = HTMLTestRunner(stream=fp,
                            title="大标题：测试报告",
                            description='执行测试用例如下：')
    # 查找测试文件
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_sta.py')

    runner.run(discover)
    fp.close()

    #②搜索最新生成的文件
    new_report = new_report(report_dir)
    #③发送邮件
    send_mail(new_report,new_report_fail,now)

    #展示测试报告html
    driver = driver.browser()
    driver.get("F:/PyProject/project/tcs/report/"+ now +"_result.html")

    stoptime = time.strftime('%H:%M:%S')
    print("结束时间为：%s" %stoptime)