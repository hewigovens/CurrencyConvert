#!/usr/bin/env python
# coding:utf-8

import json
import urllib2
import os
import time
import locale
from settings_local import __apikey__

__author__ = 'hewigovens'
__version__ = '1.0.1'

latest_rates = 'latest_rates.json'
popclip_text = os.getenv('POPCLIP_TEXT')
popclip_text = popclip_text.replace(',', '')
support_currency = {
    '$': 'USD',
    'USD': 'USD',
    'TWD': 'TWD',
    '£': 'GBP',
    '€': 'EUR',
    '円': 'JPY',
    'JPY': 'JPY',
    '￥': 'JPY'
}

locale.setlocale(locale.LC_ALL, 'zh_CN')
fp = None
dollars = None


def get_latest_rates():
    rates_req = urllib2.urlopen(
        'http://openexchangerates.org/api/latest.json?app_id=%s' % __apikey__)
    with open(latest_rates, 'w') as fp:
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

for currency in support_currency.keys():
    if currency in popclip_text:
        dollars = float(popclip_text.replace(
            currency, '')) / rates_json['rates'][support_currency[currency]]
        break

chinese_yuan = dollars * rates_json['rates']['CNY']

print("￥%s" % (locale.format('%.2f', chinese_yuan, grouping=True)))
fp.close
