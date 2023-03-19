def get_ele(locator):
    return f'document.querySelector("{locator}")'


def hidden(locator, index):
    js = ''
    if index:
        js = get_ele(locator) + f'[{index}]' + '.hidden = true'
    else:
        js = get_ele(locator) + '.hidden = true'
    return js


def no_hidden(locator, index):
    js = ''
    if index:
        js = get_ele(locator) + f'[{index}]' + '.hidden = false'
    else:
        js = get_ele(locator) + '.hidden = false'
    return js


def display(locator, index):
    js = ''
    if index:
        js = get_ele(locator) + f'[{index}]' + '.style.display = "block"'
    else:
        js = get_ele(locator) + '.style.display = "block"'
    return js


def no_display(locator, index):
    js = ''
    if index:
        js = get_ele(locator) + f'[{index}]' + '.style.display = "none"'
    else:
        js = get_ele(locator) + '.style.display = "none"'
    return js


def visible(locator, index):
    js = ''
    if index:
        js = get_ele(locator) + f'[{index}]' + '.style.visibility = "visible"'
    else:
        js = get_ele(locator) + '.style.visibility = "visible"'
    return js


def no_visible(locator, index):
    js = ''
    if index:
        js = get_ele(locator) + f'[{index}]' + '.style.visibility = "hidden"'
    else:
        js = get_ele(locator) + '.style.visibility = "hidden"'
    return js


def rich_text(locator, content):
    return f'document.getElementById("{locator}").contentWindow.document.body.innerHTML = "{content}"'


def scroll_to_top():
    return 'document.documentElement.scrollTop=0'


def scroll_to_bottom():
    return 'document.documentElement.scrollTop=10000'


def scroll_focus():
    """
    元素聚焦，页面会移动到元素的位置

    这种方法需要配合 webdriver 定位到的元素一起使用。

    例如：
        target = driver.find_element(By.ID, 'kw')
        driver.execute_script('arguments[0].scrollIntoView();', target)

    :return:
    """
    return 'arguments[0].scrollIntoView();'


def set_attr(locator, attr_name, attr_value, index=None):
    js = ''
    if index:
        js = get_ele(locator) + f'[{index}]' + f'.setAttribute({attr_name}, {attr_value})'
    else:
        js = get_ele(locator) + f'.setAttribute({attr_name}, {attr_value})'


def remove_attr(locator, attr_name, index=None):
    js = ''
    if index:
        js = get_ele(locator) + f'[{index}]' + f'.removeAttribute({attr_name})'
    else:
        js = get_ele(locator) + f'[{index}]' + f'.removeAttribute({attr_name})'


""" 时间控件 """