#!/usr/bin/env python   
# -*- coding: utf-8 -*-


import requests
import time


def test():
    while True:
        time.sleep(1)
        tick = time.time()
        requests.get('http://127.0.0.1:8000/api/v1.0/service/test')
        requests.get('http://127.0.0.1:8000/api/v1.0/service/image/list')
        print(tick)

if __name__ == "__main__":
    test()
