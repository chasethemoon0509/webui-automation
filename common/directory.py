import os


# directory.py 的绝对路径
directory_path = os.path.abspath(os.path.dirname(__file__))
# 项目根目录
root_path = directory_path[:directory_path.find("webui_automation")] + "webui_automation"
# 工具模块目录
utils_path = os.path.join(root_path, "utils")
# 共工模块目录
common_path = os.path.join(root_path, "common")
# 每一轮的测试，产出的日志、截图、测试报告都会放在同一个目录
output_path = os.path.join(root_path, 'output/')



