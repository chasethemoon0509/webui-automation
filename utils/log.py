import sys
import os
import time
from typing import Optional
from loguru import logger
from common.directory import output_path

log_file_directory = ''


class Log:
    def __init__(self, browser: Optional[str] = None):
        self._logger = logger
        self._logger.remove(handler_id=None)
        self._logger.add(
            sys.stderr,
            format='<lvl>{time:YYYY-MM-DD HH:mm:ss:SS} | {level} | {file} | {function} {line} ——> {message}</lvl>',
        )

        global log_file_directory
        log_file_directory = output_path + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()) + '/'

        if not os.path.exists(log_file_directory):
            os.mkdir(log_file_directory)
            if browser:
                file = log_file_directory + browser + '-{time:YYYY-MM-DD-HH-mm-ss-SS}.log'
            else:
                file = log_file_directory + '{time:YYYY-MM-DD-HH-mm-ss-SS}.log'
        else:
            if browser:
                file = log_file_directory + browser + '-{time:YYYY-MM-DD-HH-mm-ss-SS}.log'
            else:
                file = log_file_directory + '{time:YYYY-MM-DD-HH-mm-ss-SS}.log'
        self._logger.add(file, rotation='1MB')

    def get_logger(self):
        return self._logger


log = Log().get_logger()
