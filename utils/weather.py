#!/usr/bin/env python   
# -*- coding: utf-8 -*-

import requests, xpinyin
# from lxml import etree
from pyquery import PyQuery as pq

base_url = "https://www.tianqi.com/"

def get_weather(name):
    result = dict()
    result['name'] = "城市输入有误"
    result['temperature'] = None
    result['wind_direction'] = None
    result['wind_strength'] = None
    result['humidity'] = None
    result['time'] = None
    user_agent = {'User-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36                    Edge/17.17134"}
    if isinstance(name, str):
        name = name.strip()
        if name.endswith('市'):
            name = name[:-1]
            city_name = xpinyin.Pinyin().get_pinyin(name,"")
            url = base_url + city_name
            response = requests.get(url, headers=user_agent)
            if response.status_code == 200:
                doc = pq(response.text)
                weather_node = doc("dl.weather_info dd")
                result['name'] = weather_node('.name h2').text()
                result['temperature'] = weather_node('.weather p').text()
                result['wind_direction'] = weather_node('.shidu b:nth-child(2)').text()[3:].split(" ")[0]
                result['wind_strength'] = weather_node('.shidu b:nth-child(2)').text()[3:].split(" ")[1]
                result['humidity'] = weather_node('.shidu b:nth-child(1)').text()[3:]
                result['time'] = weather_node('.week').text().split('\u3000')[0]
                print(result)
                return result
            else:
                # print(result)
                return result
    else:
        # print(result)
        return result

if __name__ == "__main__":
    get_weather("广州")