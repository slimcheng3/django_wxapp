#!/usr/bin/env python   
# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq
from random import randint

def random_joke():
    index = randint(1,999)
    user_agent = {
        'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36                    Edge/17.17134"}
    url = "http://haha.sogou.com/tag/li/冷笑话/new/" + str(index)
    response = requests.get(url=url, headers=user_agent)
    doc = pq(response.text)
    # print(doc)
    itemlist = doc('div.hlist#ind-list .ce')
    # print(itemlist)

    data = []
    for item in itemlist.items():
        result = {}
        content = item('div.hc-c .inner div:nth-child(1)').attr('class')
        if content == "hcc-pic":
            result["ispic"] = True
            result["title"] = item('div.hc-t .hc-tit.cf').text()
            result["content"] = item('div.hc-c .inner div:nth-child(1) .pic >div').attr('img_url')
            data.append(result)
        elif content == "hcc-text":
            result["ispic"] = False
            result["title"] = item('div.hc-t .hc-tit.cf').text()
            result["content"] = item('div.hc-c .inner div:nth-child(1)').text()[:-3]
            data.append(result)
    # print(data)
    return data


if __name__ == "__main__":
    random_joke()