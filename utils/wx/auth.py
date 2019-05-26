#!/usr/bin/env python   
# -*- coding: utf-8 -*-


import json, requests
import test_weather.settings
from utils import proxy
from authorization.models import User

def c2s(appid, code):
    return code2session(appid, code)

'''
return data 的格式
{
  "session_key": "JmRNs6uPEpFzlMRmg4NqJQ==",
  "expires_in": 7200,
  "openid": "oXSML0ZH05BItFTFILfgCGxXxxik"
}
'''
def code2session(appid, code):
    API = 'https://api.weixin.qq.com/sns/jscode2session'
    params = 'appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % \
             (appid, test_weather.settings.WX_APP_SECRET, code)
    url = API + '?' + params
    response = requests.get(url=url, proxies=proxy.proxy())
    data = json.loads(response.text)
    print(data)
    return data

def already_authorized(request):
    is_authorized = False
    print("1")
    if request.session.get('is_authorized'):
        print("2")
        is_authorized = True
        print("is_authorized is true")
    return is_authorized

def get_user(request):
    if not already_authorized(request):
        raise Exception("not authoried request")
    openid = request.session.get('openid')
    user = User.objects.filter(openid=openid)[0]
    return user



