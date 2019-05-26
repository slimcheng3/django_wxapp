#!/usr/bin/env python   
# -*- coding: utf-8 -*-

from authorization.views import test_session, authorize, get_status, UserView,logout
from django.urls import path, include


urlpatterns = [
    path('test', test_session),
    path('authorize', authorize),
    path('status', get_status),
    path('user', UserView.as_view()),
    path('logout', logout)
]
