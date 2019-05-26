#!/usr/bin/env python   
# -*- coding: utf-8 -*-

import os, yaml, django, hashlib
from test_weather import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','test_weather.settings')
django.setup()

from apis.models import App

def init_app_data():
    old_apps = App.objects.all()
    path = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(path, 'r', encoding='utf-8') as f:
        apps = yaml.load(f)
        published = apps.get('published')
        for item in published:
            item = item.get('app')
            src = item.get('category') + item.get('application')
            appid = hashlib.md5(src.encode('utf8')).hexdigest()
            if len(App.objects.filter(appid=appid)) == 1:
                app = App.objects.filter(appid=appid)[0]
            else:
                app = App()
            app.appid = appid
            app.name = item.get('name')
            print(app.name)
            app.application = item.get('application')
            app.url = item.get('url')
            app.publish_date = item.get('publish_date')
            app.category = item.get('category')
            app.desc = item.get('desc')
            app.save()

if __name__ == "__main__":
    init_app_data()



