#!/usr/bin/env python   
# -*- coding: utf-8 -*-

from django.urls import path, include

urlpatterns = [
    path('service/', include('apis.urls')),
    path('auth/', include('authorization.urls'))
]