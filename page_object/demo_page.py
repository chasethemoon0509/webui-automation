from selenium.webdriver.common.by import By
from common.page import Page
from page_locator.demo_page_locator import *
from common.directory import root_path


class DemoPage(Page):
    def login(self, account, password):
        self.open_url(f'{root_path}\index.html')
        self.input(account_input_ele, account, timeout=5)
        self.input(password_input_ele, password, timeout=5)
        self.click(submit_ele, timeout=5)



