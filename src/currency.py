#!/usr/bin/env python3
# coding:utf-8

import json
import urllib.request
import os
import time
import locale
import sys

from settings_local import __apikey__
from collections import OrderedDict

__author__ = 'hewigovens'
__version__ = '1.0.1'

latest_rates = 'latest_rates.json'
popclip_text = os.getenv('POPCLIP_TEXT')
if not popclip_text:
    popclip_text = "100$"

popclip_text = popclip_text.replace(',', '')
support_currency = OrderedDict([
    ('USD', 'USD'),
    ('TWD', 'TWD'),
    ('NT', 'TWD'),
    ('HK$', 'HKD'),
    ('$', 'USD'),
    ('£', 'GBP'),
    ('€', 'EUR'),
    ('円', 'JPY'),
    ('JPY', 'JPY'),
    ('￥', 'JPY')
])

locale.setlocale(locale.LC_ALL, 'zh_CN')
fp = None
dollars = None


def get_latest_rates():
    response = urllib.request.urlopen(
        'https://openexchangerates.org/api/latest.json?app_id=%s' % __apikey__)
    with open(latest_rates, 'wb') as fp:
        fp.write(response.read())

def main():
    if not os.path.exists(latest_rates):
        get_latest_rates()

    time_now = int(time.time())
    timestamp = float("inf")
    rates_json = None
    try:
        fp = open(latest_rates)
        rates_json = json.load(fp)
        timestamp = rates_json['timestamp']
    except:
        pass
    finally:
        if time_now - timestamp >= 86400:
            fp.close()
            get_latest_rates()
            fp = open(latest_rates)
            rates_json = json.load(fp)

    for currency in support_currency.keys():
        if currency in popclip_text:
            dollars = float(popclip_text.replace(
                currency, '').replace(' ', '')) / rates_json['rates'][support_currency[currency]]
            break

    chinese_yuan = dollars * rates_json['rates']['CNY']
    print("￥%s" % (locale.format_string('%.2f', chinese_yuan, grouping=True)))
    fp.close()

if __name__ == '__main__':
    main()
