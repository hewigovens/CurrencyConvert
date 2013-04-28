#!/usr/bin/env python
# coding:utf-8

import json
#import requests
import urllib2
import os
import time

__author__ = 'hewigovens'
__apikey__ = ''

latest_rates = 'latest_rates.json'
popclip_text = os.getenv('POPCLIP_TEXT')
fp = None

def get_latest_rates():
    #rates_req = requests.get('http://openexchangerates.org/api/latest.json?app_id=%s' % __apikey__)
    rates_req = urllib2.urlopen('http://openexchangerates.org/api/latest.json?app_id=%s' % __apikey__)
    with open(latest_rates,'w') as fp:
        fp.writelines(''.join(rates_req.readlines()))

if not os.path.exists(latest_rates):
    get_latest_rates()

time_now = int(time.time())
fp = open(latest_rates)
rates_json = json.load(fp)
timestamp = rates_json['timestamp']
if time_now - timestamp >= 86400:
    fp.close()
    get_latest_rates()
    fp = open(latest_rates)
    rates_json = json.load(fp)

dollars = float(popclip_text.replace('$',''))
chinese_yuan = dollars * rates_json['rates']['CNY']

print "￥%.2f" % chinese_yuan

fp.close()
