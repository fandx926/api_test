import unittest
# noinspection PyUnresolvedReferences
import logging
from api_test.config.config_test import *
from api_test.config.config_test import report_file, test_path
from api_test.lib.HTMLTestRunner import HTMLTestRunner
from api_test.lib.send_email import send_email  # 修改导入路径

logging.info("================================== 测试开始 ==================================")
suite = unittest.defaultTestLoader.discover(test_path)

with open(report_file, 'wb') as f:  # 从配置文件中读取
    HTMLTestRunner(stream=f, title="Api Test", description="测试描述",).run(suite)

send_email(report_file)  # 从配置文件中读取
logging.info("================================== 测试结束 ==================================")
