#!/usr/bin/env python   
# -*- coding: utf-8 -*-



import test_weather.settings


def proxy():
    if test_weather.settings.USE_PROXY:
        # add your proxy here
        return {}
    else:
        return {}
