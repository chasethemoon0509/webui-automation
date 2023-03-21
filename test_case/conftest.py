import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from common.directory import root_path
import yaml


@pytest.fixture(scope='class')
def get_driver(request):
    """
    实例化 driver 对象并返回，当没有对象调用此 fixture 时，再执行 yield 后面的语句，后面的语 句大多数都是测试清理操作。

    和此 conftest.py 文件在同一目录中的测试用例都可以调用这个 fixture
    :return:
    """
    browser = request.config.getoption('--browser')

    if browser.lower() == 'chrome':
        exe_path = Service(r'D:\Python37\chromedriver.exe')
        driver = webdriver.Chrome(service=exe_path)
        yield driver
        driver.close()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox(firefox_binary=r'C:\Program Files\Mozilla Firefox\firefox.exe')
        yield driver
        driver.close()
    """
        有时候因为某些原因，我们不想所有用例都从登录开始执行，或者是因为 web 项目采用了比较麻烦的登录验证方式，不容易处理。

        所以我们想绕过登录，但是 web 项目上又必须存在登录的状态。

        有一种方法可以解决问题：

                            我们可以先手动登录，登录成功之后复制需要用到的 cookie 等数据。

                            然后再使用 webdriver 对象的 add_cookie() 方法把上一步得到的 cookie 添加进去。
                            
                            再执行用例时，最好在用例里添加刷新页面的操作。
                            
                            另外我们还可以根据实际情况结合 requests 库来实现，使用 requests 库获取到 token，然后把 token 写入 cookie 中。
                            
                            对于比较麻烦的登录验证（图形验证或滑块验证等），还可以让研发人员协助，例如加一个白名单校验，白名单内的用户不需要进行图形验证或滑块验证等
                            
                            
    """






