#!/usr/bin/env python   
# -*- coding: utf-8 -*-
import datetime

def get_rest_day_insecond():
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    left = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 0, 0, 0) - now
    return int(left.total_seconds())