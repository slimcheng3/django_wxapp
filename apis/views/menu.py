#!/usr/bin/env python   
# -*- coding: utf-8 -*-

import yaml
from test_weather import settings
from django.http import JsonResponse
import os
import utils.response
from apis.models import App
from django.views import View
from utils.response import CommonResponseMixin, ReturnCode
from authorization.models import User
from utils.wx.auth import already_authorized, get_user
import json


def init_app_data():
    data_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(data_file, 'r', encoding='utf-8') as f:
        apps = yaml.load(f)
        # print(apps.get("published"))
        return apps

def get_menu(request):
    # global_app_data = init_app_data()
    # published_app_data = global_app_data.get("published")
    # response = utils.response.wrap_json_response(data=published_app_data, code=utils.response.ReturnCode.SUCCESS)
    apps = App.objects.all()
    data = []
    for app in apps:
        data.append(app.to_dict())
    response = utils.response.wrap_json_response(data=data)
    return JsonResponse(data=response, safe=False)


class UserMenu(View, CommonResponseMixin):
    def get(self, request):
        if not already_authorized(request):
            resposne = self.wrap_json_response(code=ReturnCode.UNAUTHORIZED)
            return JsonResponse(data=resposne, safe=False)
        else:
            user = get_user(request)
            menu_list = user.menu.all()
            data = []
            for menu in menu_list:

                data.append(menu.to_dict())
            print("111",data)
            resposne = self.wrap_json_response(data=data,code=ReturnCode.SUCCESS)
            return JsonResponse(data=resposne, safe=False)

    def post(self, request):
        if not already_authorized(request):
            resposne = self.wrap_json_response(code=ReturnCode.UNAUTHORIZED)
            return JsonResponse(data=resposne, safe=False)
        else:
            user = get_user(request)
            post_menu = json.loads(request.body.decode('utf-8'))
            post_menu = post_menu.get('data')
            apps = []
            for menu in post_menu:
                appid = menu.get('appid')
                menu = App.objects.filter(appid=appid)[0]
                apps.append(menu)
            user.menu.set(apps)
            user.save()
            resposne = self.wrap_json_response(code=ReturnCode.SUCCESS)
            return JsonResponse(data=resposne, safe=False)










if __name__ == "__main__":
    init_app_data()