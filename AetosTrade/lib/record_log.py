#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time
import os
import logging
import logging.handlers
class RecordLog:
    def log_output(self):
        LOG_DIR = 'log'
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
        logger = logging.getLogger('process')
        logger.setLevel(logging.DEBUG)
        handler = logging.handlers.TimedRotatingFileHandler(
            os.path.join(os.path.abspath("./log"), "process_%s.log" % time.strftime("%Y-%m-%d %H-%M-%S")), 'D')
        handler.setLevel(logging.DEBUG)
        process_formatter = logging.Formatter(
            '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        handler.setFormatter(process_formatter)

        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)

        console_formatter = logging.Formatter('%(asctime)s:%(message)s')
        console.setFormatter(console_formatter)

        logger.addHandler(console)
        logger.addHandler(handler)
        return logger