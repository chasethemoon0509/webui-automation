"""
存放对应页面的元素对象，包括元素属性值和定位器
"""
from selenium.webdriver.common.by import By
# 账号输入框
account_input_ele = (By.ID, 'account')
# 密码输入框
password_input_ele = (By.ID, 'password')
# 登录按钮
submit_ele = (By.CSS_SELECTOR, 'input[value="登录"]')
# 结果显示标签
login_result_ele = (By.CLASS_NAME, 'login_result')

