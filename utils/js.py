"""
常用的 js 语句
"""


def get_ele(ele):
    """
    查找元素
    :param ele: 元素
    :return:
    """
    return f'document.querySelector("{ele}")'


def hidden(ele, index=None):
    """
    隐藏元素，hidden
    :param ele: 元素
    :param index: 如果查找到多个相同属性的元素，需要指定具体隐藏哪个元素
    :return: 
    """
    js = ''
    if index:
        js = get_ele(ele) + f'[{index}]' + '.hidden = true'
    else:
        js = get_ele(ele) + '.hidden = true'
    return js


def no_hidden(ele, index=None):
    """
    取消隐藏元素，hidden
    :param ele: 元素
    :param index: 如果查找到多个相同属性的元素，需要指定具体取消隐藏哪个元素
    :return:
    """
    js = ''
    if index:
        js = get_ele(ele) + f'[{index}]' + '.hidden = false'
    else:
        js = get_ele(ele) + '.hidden = false'
    return js


def display(ele, index=None):
    """
    展示元素，display
    :param ele: 元素
    :param index: 如果查找到多个相同属性的元素，需要指定具体展示哪个元素
    :return:
    """
    js = ''
    if index:
        js = get_ele(ele) + f'[{index}]' + '.style.display = "block"'
    else:
        js = get_ele(ele) + '.style.display = "block"'
    return js


def no_display(ele, index=None):
    """
    不展示元素，display
    :param ele: 元素
    :param index: 如果查找到多个相同属性的元素，需要指定具体不展示哪个元素
    :return:
    """
    js = ''
    if index:
        js = get_ele(ele) + f'[{index}]' + '.style.display = "none"'
    else:
        js = get_ele(ele) + '.style.display = "none"'
    return js


def visible(ele, index=None):
    """
    展示元素, visible
    :param ele: 元素
    :param index: 如果查找到多个相同属性的元素，需要指定具体展示哪个元素
    :return:
    """
    js = ''
    if index:
        js = get_ele(ele) + f'[{index}]' + '.style.visibility = "visible"'
    else:
        js = get_ele(ele) + '.style.visibility = "visible"'
    return js


def no_visible(ele, index=None):
    """
    不展示元素, visible
    :param ele: 元素
    :param index: 如果查找到多个相同属性的元素，需要指定具体不展示哪个元素
    :return:
    """
    js = ''
    if index:
        js = get_ele(ele) + f'[{index}]' + '.style.visibility = "hidden"'
    else:
        js = get_ele(ele) + '.style.visibility = "hidden"'
    return js


def rich_text(ele, content):
    """
    给富文本编辑器插入内容
    :param ele: 元素
    :param content: 要插入的内容
    :return:
    """
    return f'document.getElementById("{ele}").contentWindow.document.body.innerHTML = "{content}"'


def scroll_to_top():
    """
    控制页面滚动条，滚动到最顶部
    :return:
    """
    return 'document.documentElement.scrollTop=0'


def scroll_to_bottom():
    """
    控制页面滚动条，滚动到最底部
    :return:
    """
    return 'document.documentElement.scrollTop=10000'


def scroll_focus():
    """
    控制页面滚动条，滚动到目标元素所在的区域，元素聚焦，页面会移动到元素的位置

    这种方法需要配合 webdriver 定位到的元素一起使用。

    例如：
        target = driver.find_element(By.ID, 'kw')
        driver.execute_script('arguments[0].scrollIntoView();', target)
    :return:
    """
    return 'arguments[0].scrollIntoView();'


def set_attr(ele, attr_name, attr_value, index=None):
    """
    设置、修改元素属性
    :param ele: 元素
    :param attr_name: 属性名
    :param attr_value: 属性值
    :param index: 如果查找到多个相同属性的元素，需要指定具体哪个元素
    :return:
    """
    js = ''
    if index:
        js = get_ele(ele) + f'[{index}]' + f'.setAttribute({attr_name}, {attr_value})'
    else:
        js = get_ele(ele) + f'.setAttribute({attr_name}, {attr_value})'


def remove_attr(ele, attr_name, index=None):
    """
    删除元素属性
    :param ele: 元素
    :param attr_name: 属性名
    :param index: 如果查找到多个相同属性的元素，需要指定具体哪个元素
    :return:
    """
    js = ''
    if index:
        js = get_ele(ele) + f'[{index}]' + f'.removeAttribute({attr_name})'
    else:
        js = get_ele(ele) + f'[{index}]' + f'.removeAttribute({attr_name})'

