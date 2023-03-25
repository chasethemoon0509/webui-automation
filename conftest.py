"""
项目整体层面的 conftest.py，区别于测试用例层面的 conftest.py

这里暂时只实现自定义参数、和测试结果的简单统计
"""
from utils.send_email import send_email


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


def pytest_terminal_summary(terminalreporter):
    """
    这个钩子函数收集测试结果数据
    """
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    xfailed = len(terminalreporter.stats.get('xfailed', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    """
    最后将大致的测试结果数据传给邮件发送方法
    """
    send_email(total, passed, failed, xfailed, skipped)

