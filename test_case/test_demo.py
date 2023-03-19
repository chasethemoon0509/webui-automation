import time
import pytest
from page_object.demo_page import DemoPage
from selenium import webdriver
from utils.log import log
from page_locator.demo_page_locator import login_result_ele


@pytest.mark.usefixtures('get_driver')
class TestDemo:
    @pytest.mark.parametrize('account, password', [('a123456789', 'a123456789'), ('aaaaaaaaa', 'aaaaaaaaa'), ('123456789', '123456789')])
    def test_1(self, account, password, get_driver):
        log.info('🚀执行用例: test_1')
        DemoPage(get_driver).login(account, password)
        DemoPage(get_driver).ast_eq(DemoPage(get_driver).find(login_result_ele, timeout=5).text, '登录结果：成功', login_result_ele)

