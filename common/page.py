"""
页面基类，封装所有页面都会用到的操作
"""
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.log import log, log_file_directory
import pyautogui


class Page:
    def __init__(self, driver):
        """
        接收 webdriver 对象
        :param driver:
        """
        self.driver = driver

    def open_url(self, url):
        """
        打开项目或某个页面
        :param url: 页面 url 地址
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def wait(self, locator, timeout, poll_frequency=1, ignored_exceptions=None):
        """
        等待元素
        :param locator: 元素对象
        :param timeout: 超时时间
        :param poll_frequency: 轮询间隔
        :param ignored_exceptions: 可忽略的异常
        :return:
        """
        try:
            log.info('第一步: 等待元素 {} 出现', locator)
            return WebDriverWait(
                self.driver,
                timeout=timeout,
                poll_frequency=poll_frequency,
                ignored_exceptions=ignored_exceptions
            ).until(ec.visibility_of_element_located(locator))
        except Exception as e:
            log.error('第一步: 等待元素 {}, 结果报错: {}', locator, e)
            raise

    def wait_page_url(self, url, timeout, poll_frequency=1, ignored_exceptions=None):
        """
        等待预期的 url
        :param url: 预期的 url
        :param timeout: 超时时间
        :param poll_frequency: 轮询间隔
        :param ignored_exceptions: 可忽略的异常
        :return:
        """
        try:
            log.info('第一步: 等待 url {} 出现', url)
            return WebDriverWait(
                self.driver,
                timeout=timeout,
                poll_frequency=poll_frequency,
                ignored_exceptions=ignored_exceptions
            ).until(ec.url_to_be(url))
        except Exception as e:
            log.error('第一步: 等待 url {}, 结果报错: {}', url, e)
            raise

    def find(self, locator, timeout, poll_frequency=1, ignored_exceptions=None):
        """
        定位、查找元素（单个）
        :param locator: 元素对象
        :param timeout: 超时时间
        :param poll_frequency: 轮询间隔
        :param ignored_exceptions: 可忽略的异常
        :return:
        """
        self.wait(locator, timeout=timeout, poll_frequency=poll_frequency, ignored_exceptions=ignored_exceptions)
        try:
            log.info('第二步: 定位元素 {}', locator[1])
            return self.driver.find_element(*locator)
        except Exception as e:
            log.error('第二步: 定位元素 {}, 结果报错: {}', locator[1], e)
            raise

    def find_s(self, locator, timeout, poll_frequency=1, ignored_exceptions=None):
        """
        定位、查找元素（多个）
        :param locator: 元素对象
        :param timeout: 超时时间
        :param poll_frequency: 轮询间隔
        :param ignored_exceptions: 可忽略的异常
        :return:
        """
        self.wait(locator, timeout=timeout, poll_frequency=poll_frequency, ignored_exceptions=ignored_exceptions)
        try:
            log.info('第二步: 定位多个元素 {}', locator[1])
            return self.driver.find_elements(*locator)
        except Exception as e:
            log.error('第二步: 定位多个元素 {}, 结果报错: {}', locator[1], e)
            raise

    def click(self, locator, timeout, poll_frequency=0, ignored_exceptions=None):
        """
        点击元素
        :param locator: 元素对象
        :param timeout: 超时时间
        :param poll_frequency: 轮询间隔
        :param ignored_exceptions: 可忽略的异常
        :return:
        """
        try:
            log.info('⚔功能操作: 点击元素 {}', locator[1])
            self.find(locator, timeout, poll_frequency=poll_frequency, ignored_exceptions=ignored_exceptions).click()
        except Exception as e:
            log.error('⚔功能操作: 点击元素 {}, 结果报错: {}', locator[1], e)
            raise
        else:
            return self

    def input(self, locator, text, timeout, poll_frequency=1, ignored_exceptions=None):
        """
        输入操作
        :param locator: 元素对象
        :param text: 要输入的字符串
        :param timeout: 超时时间
        :param poll_frequency: 轮询间隔
        :param ignored_exceptions: 可忽略的异常
        :return:
        """
        try:
            log.info('⚔功能操作: 输入字符 {}', text)
            self.find(
                locator,
                timeout,
                poll_frequency=poll_frequency,
                ignored_exceptions=ignored_exceptions
            ).send_keys(text)
        except Exception as e:
            log.info('⚔功能操作: 输入字符 {}, 结果报错: {}', text, e)
            raise
        else:
            return self

    """ 浏览器信息 """
    def page_title(self):
        """
        返回页面标题
        :return:
        """
        log.info('当前页面标题: {}', self.driver.title)
        return self.driver.title

    def page_url(self):
        """
        返回页面 url
        :return:
        """
        log.info('当前页面 url: {}', self.driver.current_url)
        return self.driver.current_url

    """ 浏览器导航 """
    def back(self):
        """
        返回上一页
        :return:
        """
        log.info('返回上一个页面')
        self.driver.back()
        log.info('返回之后，当前页面标题: {}, url: {}', self.driver.title, self.driver.current_url)
        return self

    def forward(self):
        """
        前往下一页
        :return:
        """
        log.info('前往下一个页面')
        self.driver.back()
        log.info('前进之后，当前页面标题: {}, url: {}', self.driver.title, self.driver.current_url)
        return self

    def refresh(self):
        """
        刷新页面
        :return:
        """
        log.info('刷新页面')
        self.driver.refresh()
        return self

    """ 警告框、提示框和确认框"""
    def wait_alert(self, timeout):
        """
        等待警告框
        :param timeout: 超时时间
        :return:
        """
        try:
            log.info('等待警告框')
            alert = WebDriverWait(self.driver, timeout=timeout).until(ec.alert_is_present())
            return alert
        except Exception as e:
            log.error('警告框未出现: {}', e)
            raise

    def alert_accept(self, timeout):
        """
        在警告框上点击确认按钮
        :param timeout: 超时时间
        :return:
        """
        self.wait_alert(timeout).accept()
        return self

    def wait_confirm(self, timeout):
        """
        等待确认框
        :param timeout: 超时时间
        :return:
        """
        try:
            log.info('等待确认框')
            confirm = WebDriverWait(self.driver, timeout=timeout).until(ec.alert_is_present())
            return confirm
        except Exception as e:
            log.error('确认框未出现: {}', e)
            raise

    def confirm_accept(self, timeout):
        """
        在确认框上点击确认按钮
        :param timeout: 超时时间
        :return:
        """
        self.wait_confirm(timeout).accept()
        return self

    def wait_prompt(self, timeout):
        """
        等待提示框
        :param timeout: 超时时间
        :return:
        """
        try:
            log.info('等待提示框')
            prompt = WebDriverWait(self.driver, timeout=timeout).until(ec.alert_is_present())
            return prompt
        except Exception as e:
            log.error('提示框未出现: {}', e)
            raise

    def prompt_accept(self, timeout):
        """
        在提示框上点击确认按钮
        :param timeout: 超时时间
        :return:
        """
        self.wait_prompt(timeout).accept()
        return self

    def prompt_dismiss(self, timeout):
        """
        在提示框上点击取消按钮
        :param timeout: 超时时间
        :return:
        """
        self.wait_prompt(timeout).dismiss()
        return self

    def prompt_input(self, timeout, text):
        """
        在提示框中输入字符串
        :param timeout: 超时时间
        :param text: 要输入的字符串
        :return:
        """
        self.wait_prompt(timeout).send_keys(text)
        return self

    """ frames """
    def switch_frame(self, locator, timeout):
        """
        进入 frame
        :param locator: 元素对象
        :param timeout: 超时时间
        :return:
        """
        try:
            frame = self.find(locator, timeout)
            if frame:
                log.info('进入 frame: {}', locator)
                self.driver.switch_to.frame(frame)
        except Exception as e:
            log.error('进入 frame: {}, 错误: {}', locator, e)

    def switch_frame_by_index(self, locator, timeout, index):
        """
        存在多个 frmae，指定进入哪个 frame
        :param locator: 元素对象
        :param timeout: 超时时间
        :param index: 目标 frame 下标
        :return:
        """
        try:
            frame = self.find_s(locator, timeout)[index]
            if frame:
                log.info('进入 frame: {}', locator)
                self.driver.switch_to.frame(frame)
        except Exception as e:
            log.error('进入 frame: {}, 错误: {}', locator, e)

    def leave_frame(self):
        """
        切出 frame
        :return:
        """
        self.driver.switch_to.default_content()
        log.info('已切出 frame')

    """ 窗口和标签页  """
    @property
    def current_window(self):
        """
        返回当前窗口对象信息
        :return:
        """
        current = self.driver.current_window_handle
        log.info('当前窗口: {}', current)
        return current

    @property
    def all_window(self):
        """
        返回当前存在的所有窗口
        :return:
        """
        handles = self.driver.window_handles
        log.info('窗口总数: {}, 窗口列表: {}', len(handles), handles)
        return handles

    def switch_window(self):
        """
        切换到下一个窗口
        :return:
        """
        try:
            log.info('切换窗口')
            all_w = self.all_window()
            current_w = self.current_window()
            for w in all_w:
                if w != current_w:
                    self.driver.switch_to.window(w)
                    break
        except Exception as e:
            log.error('切换窗口失败: {}', e)

    def switch_window_by_index(self, index):
        """
        切换到指定的窗口
        :param index: 窗口下标（顺序）
        :return:
        """
        try:
            log.info('切换到第 {} 个窗口', index)
            all_w = self.all_window()
            self.driver.switch_to.window(all_w[index])
        except Exception as e:
            log.error('切换到第 {} 个窗口失败: {}', index, e)

    @property
    def window_size(self):
        """
        返回当前窗口的尺寸
        :return:
        """
        size = self.driver.get_window_size()
        return size

    """ 屏幕截图 """
    def screenshot(self, file_name):
        """
        整屏截图
        :param file_name: 截图文件名称
        :return:
        """
        try:
            log.info('开始整屏截图')
            self.driver.save_screenshot(log_file_directory + '/{}.png'.format(file_name))
        except Exception as e:
            log.info('整屏截图出错: {}', e)

    def screenshot_ele(self, locator, timeout, file_name):
        """
        元素截图，只截取元素所在的区域
        :param locator: 元素对象
        :param timeout: 超时时间
        :param file_name: 截图文件名称
        :return:
        """
        try:
            log.info('开始元素截图')
            self.find(locator, timeout).screenshot(log_file_directory + '/{}.png'.format(file_name))
        except Exception as e:
            log.error('元素截图出错: {}', e)

    """ 执行 js 脚本 """
    def execute_js(self, js):
        """
        执行 js
        :param js: js 语句
        :return:
        """
        try:
            log.info('执行 js 脚本: {}', js)
            self.driver.execute_script(js)
        except Exception as e:
            log.error('执行 js 脚本 {}, 出错: {}', js, e)

    """ 文件上传 """
    def upload(self, locator, timeout, way, file_path):
        """
        兼顾 send_keys() 方法上传和使用第三方库提供的方法上传
        :return:
        """
        if way == 1:
            self.find(locator, timeout).send_keys(file_path)
        elif way == 2:
            self.click(locator, timeout)
            pyautogui.write(file_path)
            pyautogui.press('enter', 2)

    """ 断言 """
    def ast_eq(self, a, b, locator):
        """
        断言两个对象是否相等，并将结果写入日志，断言失败时会调用截图方法
        :param a: 断言对象（预期或实际）
        :param b: 断言对象（预期或实际）
        :param locator: 元素对象
        :return:
        """
        file_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        try:
            log.info('开始断言 {} 和 {} 是否相等', a, b)
            assert a == b
        except Exception as e:
            log.error('断言结果: {} 和 {} 不相等', a, b)
            self.screenshot_ele(locator, file_name=file_name, timeout=5)
            raise


