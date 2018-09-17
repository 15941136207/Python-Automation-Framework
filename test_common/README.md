浏览器及url的基础配置
os.path.abspath('test.csv')
页面基础类base_page:封装了selenium库中常用的方法，包括对象查找，截图输出，浏览器的前进后退，清除和输入... 
浏览器引擎类browser_engine:通过读取配置文件去选择浏览器和url，并返回浏览器对象实例 
日志类 Logger: 封装日志输出及控制台输出方法