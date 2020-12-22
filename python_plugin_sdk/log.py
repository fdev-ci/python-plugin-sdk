# -*- coding: utf-8 -*-

import sys
import logging

LOG_NAME = "PLUGIN_LOG"
LOG_FORMAT = "%(message)s"
LOG_LEVEL = logging.DEBUG


def getLogger():
    """
    兼容老版本的方法
    """
    return logger().logger


class logger():

    def __init__(self):
        init_logger = logging.getLogger(LOG_NAME)
        if init_logger.handlers:
            self.logger = init_logger
        else:
            init_logger.setLevel(LOG_LEVEL)
            formatter = logging.Formatter(LOG_FORMAT)
            console = logging.StreamHandler(sys.stdout)
            console.setFormatter(formatter)
            init_logger.addHandler(console)
            self.logger = init_logger

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)


if __name__ == '__main__':
    obj = logger()
    obj.info("info is info" + " luotao")
    obj.debug("debug is debug")
    obj.warning("warning is warning")
    obj.error("error is error")
