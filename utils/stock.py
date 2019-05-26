#!/usr/bin/env python   
# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq

def get_stock(stock):
    result = {}
    user_agent = {
        'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36                    Edge/17.17134"}
    if stock.get("market") == 'sz':
        code = stock.get("code")
        url = 'http://www.szse.cn/api/market/ssjjhq/getTimeData?marketId=1&code=' + str(code)
        response = requests.get(url=url,headers=user_agent).json()
        data = response.get("data")
        result["name"] = data.get("name")
        result["open"] = data.get("open")
        result["now"] = data.get("now")
        result["high"] = data.get("high")
        result["low"] = data.get("low")
        result["isrising"] = data.get("now") > data.get("open")
        print(result.get("now"))
        print(result.get("open"))
        sub = abs(float(data.get("now")) - float(data.get("open")))
        result["sub"] = float("%.2f" % sub)
        print(result)
        return result
    elif stock.get("market") == 'sh':
        code = stock.get("code")
        url = 'https://hq.gucheng.com/SH' + str(code)
        response = requests.get(url=url, headers=user_agent)
        doc = pq(response.text)
        data = doc('section.stock_price.clearfix')
        result["name"] = stock.get("name")
        result["open"] = data('div.s_date dl:nth-child(1) dd.color_up').text()
        result["now"] = data('div.s_price em:nth-child(1)').text()
        result["high"] = data('dl.s_height dd.color_up').text()
        result["low"] = data('dl.s_height dd.down').text()
        result["isrising"] = result.get("now") > result.get("open")
        print(result.get("now"))
        print(result.get("open"))
        sub = abs(float(result.get("now")) - float(result.get("open")))
        result["sub"] = float("%.2f" % sub)
        print(result)
        return result

if __name__ == "__main__":
    stock = {
        "name": "工商银行",
        "market": "sh",
        "code": "601398"
    }
    get_stock(stock)