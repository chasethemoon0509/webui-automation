import datetime
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.log import log, log_file_directory
import inspect
import traceback


class Page:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def wait(self, locator, timeout, poll_frequency=1, ignored_exceptions=None):
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
        self.wait(locator, timeout=timeout, poll_frequency=poll_frequency, ignored_exceptions=ignored_exceptions)
        try:
            log.info('第二步: 定位元素 {}', locator[1])
            return self.driver.find_element(*locator)
        except Exception as e:
            log.error('第二步: 定位元素 {}, 结果报错: {}', locator[1], e)
            raise

    def find_s(self, locator, timeout, poll_frequency=1, ignored_exceptions=None):
        self.wait(locator, timeout=timeout, poll_frequency=poll_frequency, ignored_exceptions=ignored_exceptions)
        try:
            log.info('第二步: 定位多个元素 {}', locator[1])
            return self.driver.find_elements(*locator)
        except Exception as e:
            log.error('第二步: 定位多个元素 {}, 结果报错: {}', locator[1], e)
            raise

    def click(self, locator, timeout, poll_frequency=0, ignored_exceptions=None):
        try:
            log.info('⚔功能操作: 点击元素 {}', locator[1])
            self.find(locator, timeout, poll_frequency=poll_frequency, ignored_exceptions=ignored_exceptions).click()
        except Exception as e:
            log.error('⚔功能操作: 点击元素 {}, 结果报错: {}', locator[1], e)
            raise
        else:
            return self

    def input(self, locator, text, timeout, poll_frequency=1, ignored_exceptions=None):
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
        log.info('当前页面标题: {}', self.driver.title)
        return self.driver.title

    def page_url(self):
        log.info('当前页面 url: {}', self.driver.current_url)
        return self.driver.current_url

    """ 浏览器导航 """
    def back(self):
        log.info('返回上一个页面')
        self.driver.back()
        log.info('返回之后，当前页面标题: {}, url: {}', self.driver.title, self.driver.current_url)
        return self

    def forward(self):
        log.info('前往下一个页面')
        self.driver.back()
        log.info('前进之后，当前页面标题: {}, url: {}', self.driver.title, self.driver.current_url)
        return self

    def refresh(self):
        log.info('刷新页面')
        self.driver.refresh()
        return self

    """ 警告框、提示框和确认框"""
    def wait_alert(self, timeout):
        try:
            log.info('等待警告框')
            alert = WebDriverWait(self.driver, timeout=timeout).until(ec.alert_is_present())
            return alert
        except Exception as e:
            log.error('警告框未出现: {}', e)
            raise

    def alert_accept(self, timeout):
        self.wait_alert(timeout).accept()
        return self

    def wait_confirm(self, timeout):
        try:
            log.info('等待确认框')
            confirm = WebDriverWait(self.driver, timeout=timeout).until(ec.alert_is_present())
            return confirm
        except Exception as e:
            log.error('确认框未出现: {}', e)
            raise

    def confirm_accept(self, timeout):
        self.wait_confirm(timeout).accept()
        return self

    def wait_prompt(self, timeout):
        try:
            log.info('等待提示框')
            prompt = WebDriverWait(self.driver, timeout=timeout).until(ec.alert_is_present())
            return prompt
        except Exception as e:
            log.error('提示框未出现: {}', e)
            raise

    def prompt_accept(self, timeout):
        self.wait_prompt(timeout).accept()
        return self

    def prompt_dismiss(self, timeout):
        self.wait_prompt(timeout).dismiss()
        return self

    def prompt_input(self, timeout, text):
        self.wait_prompt(timeout).send_keys(text)
        return self

    """ frames """
    def switch_frame(self, locator, timeout):
        try:
            frame = self.find(locator, timeout)
            if frame:
                log.info('进入 frame: {}', locator)
                self.driver.switch_to.frame(frame)
        except Exception as e:
            log.error('进入 frame: {}, 错误: {}', locator, e)

    def switch_frame_by_index(self, locator, timeout, index):
        try:
            frame = self.find_s(locator, timeout)[index]
            if frame:
                log.info('进入 frame: {}', locator)
                self.driver.switch_to.frame(frame)
        except Exception as e:
            log.error('进入 frame: {}, 错误: {}', locator, e)

    def leave_frame(self):
        self.driver.switch_to.default_content()
        log.info('已切出 frame')

    """ 窗口和标签页  """
    def current_window(self):
        current = self.driver.current_window_handle
        log.info('当前窗口: {}', current)
        return current

    def all_window(self):
        handles = self.driver.window_handles
        log.info('窗口总数: {}, 窗口列表: {}', len(handles), handles)
        return handles

    def switch_window(self):
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
        try:
            log.info('切换到第 {} 个窗口', index)
            all_w = self.all_window()
            self.driver.switch_to.window(all_w[index])
        except Exception as e:
            log.error('切换到第 {} 个窗口失败: {}', index, e)

    @property
    def window_size(self):
        size = self.driver.get_window_size()
        return size

    """ 屏幕截图 """
    def screenshot(self, file_name):
        try:
            log.info('开始整屏截图')
            self.driver.save_screenshot(log_file_directory + '/{}.png'.format(file_name))
        except Exception as e:
            log.info('整屏截图出错: {}', e)

    def screenshot_ele(self, locator, timeout, file_name):
        try:
            log.info('开始元素截图')
            self.find(locator, timeout).screenshot(log_file_directory + '/{}.png'.format(file_name))
        except Exception as e:
            log.error('元素截图出错: {}', e)

    """ 执行 js 脚本 """
    def execute_js(self, js):
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
            import pyautogui
            pyautogui.write(file_path)
            pyautogui.press('enter', 2)

    """ 断言 """
    def ast_eq(self, a, b, locator):
        """
        主要用于捕获断言结果，并将结果写入日志，断言失败时会调用截图方法

        """
        file_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
        try:
            log.info('开始断言 {} 和 {} 是否相等', a, b)
            assert a == b
        except Exception as e:
            log.error('断言结果: {} 和 {} 不相等', a, b)
            self.screenshot_ele(locator, file_name=file_name, timeout=5)
            raise

    def ast_neq(self, a, b):
        """
        主要用于捕获断言结果，并将结果写入日志
        :param a:
        :param b:
        :return:
        """
        try:
            log.info('开始断言 {} 和 {} 是否不相等', a, b)
            assert a == b
        except Exception as e:
            log.error('断言结果: {} 和 {} 相等', a, b)
            raise


