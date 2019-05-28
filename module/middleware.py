#!/usr/bin/env python   
# -*- coding: utf-8 -*-

from test_weather import settings
import logging
import time

logger = logging.getLogger('statistics')
logger2 = logging.getLogger('django')

class StatisticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # logger2.info("Build the StatisticsMiddleware")

    def __call__(self, request):
        tick = time.time()
        response = self.get_response(request)
        path = request.path
        full_path = request.get_full_path()
        tock = time.time()
        cost = tock - tick
        content_list = []
        content_list.append('now=[%d]' % tock)
        content_list.append('cost=[%.6f]' % cost)
        content_list.append('path=[%s]' % path)
        content_list.append('full_path=[%s]' % full_path)
        content = settings.STATISTICS_SPLIT_FLAG.join(content_list)
        logger.info(content)
        return response


