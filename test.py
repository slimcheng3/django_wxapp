#!/usr/bin/env python   
# -*- coding: utf-8 -*-


import requests
import time

#
def test():
    while True:
        time.sleep(1)
        tick = time.time()
        requests.get('http://127.0.0.1:8000/api/v1.0/service/menu/list')
        requests.get('http://127.0.0.1:8000/api/v1.0/service/image/list')
        print(tick)
# import os, yaml, django, hashlib, logging, time
# from test_weather import settings
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','test_weather.settings')
# django.setup()
#
# logegr = logging.getLogger('statistics')
# def test():
#     while True:
#         time.sleep(5)
#         logegr.info("111")

if __name__ == "__main__":
    test()
