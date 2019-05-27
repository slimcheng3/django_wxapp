#!/usr/bin/env python   
# -*- coding: utf-8 -*-

import datetime, time
import logging
logger = logging.getLogger('django')

def demo():
    message = "Job log in crontab, now time is:" + str(datetime.datetime.now())
    print(message)
    logger.info(message)