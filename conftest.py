import pytest
from common.directory import root_path
import yaml


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='要在哪个浏览器上执行，包括 chrome、firefox、edge、ie'
    )

    parser.addoption(
        '--easyreport',
        action='store',
        default='false',
        help='生成 easy report 测试报告'
    )



# @pytest.fixture
# def a(request):
#     print('值为：', request.config.getoption('--browser'))
#     print('值为：', request.config.getoption('--easyreport'))
#
#
# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     # print(terminalreporter.stats['passed'][0].__dict__)
#
#
#     print("用例总数: ", terminalreporter._numcollected)
#     # print("详细数据：", terminalreporter.stats)
#     print(terminalreporter._session.__dict__)