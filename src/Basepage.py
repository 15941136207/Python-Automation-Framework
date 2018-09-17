import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from logs.logger import Logger

class BasePage(object):
    '''
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    '''
    def __init__(self,driver):
        self.driver = driver
        #quit browser and end testing
    def quit_browser(self):
        self.driver.quit()
        #浏览器前进操作
    def forward(self):
        self.driver.forward()
        Logger.info("click forward on current page")
        #浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page")
        #隐式等待
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds."%seconds)
    def open_url(self,url):
        self.driver.get(url)
        # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)
        # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下

        """

        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()
            

