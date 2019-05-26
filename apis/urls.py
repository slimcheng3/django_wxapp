#!/usr/bin/env python   
# -*- coding: utf-8 -*-

from apis.views import weather, menu, image, service
from django.urls import path, include

urlpatterns = [
    path('weather', weather.WeatherView.as_view()),
    path('menu/list',menu.get_menu),
    path('image/list', image.ImageViewList.as_view()),
    # path('imagetext', image.image_text),
    path('image', image.ImageView.as_view()),
    path('stock', service.StockView.as_view()),
    path('constellation', service.ConstellationView.as_view()),
    path('joke', service.JokeView.as_view()),
    path('menu/user',menu.UserMenu.as_view())
]

