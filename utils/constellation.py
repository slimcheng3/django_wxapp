#!/usr/bin/env python   
# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq
CONSTELLATIONS = {
    "白羊座": "aries",
    "金牛座": "taurus",
    "双子座": "gemini",
    "巨蟹座": "cancer",
    "狮子座": "leo",
    "处女座": "virgo",
    "天枰座": "libra",
    "天蝎座": "scorpio",
    "射手座": "sagittarius",
    "摩羯座": "capricorn",
    "水瓶座": "aquarius",
    "双鱼座": "pisces"
}

def get_constellation(item):
    user_agent = {
        'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36                    Edge/17.17134"}
    data = {}
    if CONSTELLATIONS.get(item):
        url = "https://www.xzw.com/fortune/" + CONSTELLATIONS.get(item)
        response = requests.get(url=url, headers=user_agent)
        doc = pq(response.text)
        data["content"]= doc('div.c_box div.c_cont span').text()
        data["name"] = item
        return data
    else:
        return data


if __name__ == "__main__":
    data = get_constellation("双子座")
    print(data)
