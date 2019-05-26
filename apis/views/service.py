#!/usr/bin/env python   
# -*- coding: utf-8 -*-

import json
from django.views import View
from utils.stock import get_stock
from utils.joke import random_joke
from utils.constellation import get_constellation
from utils.response import CommonResponseMixin
from django.http import JsonResponse, HttpResponse
from utils.wx import auth
from django.core.cache import cache
from utils.timeutil import get_rest_day_insecond


all_constellations = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天枰座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
popular_stocks = [
    {
        'code': '000001',
        'name': '平安银行',
        'market': 'sz'
    },
    {
        'code': '000002',
        'name': '万科A',
        'market': 'sz'
    },
    {
        'code': '600036',
        'name': '招商银行',
        'market': 'sh'
    },
    {
        'code': '601398',
        'name': '工商银行',
        'market': 'sh'
    }
]

# 股票视图
class StockView(View, CommonResponseMixin):
    def get(self, request):
        if auth.already_authorized(request):
            user = auth.get_user(request)
            focus_stocks = json.loads(user.focus_stocks)
            response = []
            for stock in focus_stocks:
                data = stock.split("-")
                data2 = {
                    "name": data[0],
                    "market": data[2],
                    "code": data[1]
                }
                result = get_stock(data2)
                result["name"] = stock
                response.append(result)
            response_data = self.wrap_json_response(data=response)
            return JsonResponse(data=response_data, safe=False)
        else:
            data = []
            for stock in popular_stocks:
                result = get_stock(stock)
                data.append(result)
            response_data = self.wrap_json_response(data=data)
            return JsonResponse(data=response_data, safe=False)


# 星座视图
class ConstellationView(View, CommonResponseMixin):
    def get(self, request):
        if auth.already_authorized(request):
            user = auth.get_user(request)
            constellations = json.loads(user.focus_constellations)
        else:
            constellations = all_constellations
        data = []
        for item in constellations:
            result = cache.get(item)
            if not result:
                print("新建缓存")
                result = get_constellation(item)
                timeout = get_rest_day_insecond()
                cache.set(item, result, timeout)
            data.append(result)
        response_data = self.wrap_json_response(data=data)
        return JsonResponse(data=response_data, safe=False)

# 每日笑话视图
class JokeView(View, CommonResponseMixin):
    def get(self, request):
        data = random_joke()
        response_data = self.wrap_json_response(data=data)
        return JsonResponse(data=response_data, safe=False)

