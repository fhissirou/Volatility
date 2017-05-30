#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import json


class HistTransaction:
    def __init__(self):
        self.URLHISTTRANSACTION= ""
        self.DATAHISTTRANSACTION=None

    def getURLHISTTRANSACTION(self):
        return self.URLHISTTRANSACTION
    def getDATAHISTTRANSACTION(self):
        return self.DATAHISTTRANSACTION

    def setURLHISTTRANSACTION(self, val):
        self.URLHISTTRANSACTION= val
    def setDATAHISTTRANSACTION(self, val):
        self.DATAHISTTRANSACTION= val

    def crawlDataHistTransaction(self):
        reponse = urllib.request.urlopen(self.getURLHISTTRANSACTION())
        body = reponse.read()
        strdata = body.decode("utf-8")
        try:
            self.setDATAHISTTRANSACTION(json.loads(strdata))
        except urllib2.HTTPError:
            pass




"""
url = "https://www.euronext.com/sites/www.euronext.com/modules/common/common_listings/custom/nyx_eu_listings/nyx_eu_listings_price_chart/pricechart/pricechart.php?q=intraday_data&from=1495411200000&isin=FR0011584549&mic=XPAR&dateFormat=15/05/2017&locale=null"
#precia 22/05
url2="https://www.euronext.com/sites/www.euronext.com/modules/common/common_listings/custom/nyx_eu_listings/nyx_eu_listings_price_chart/pricechart/pricechart.php?q=intraday_data&from=1495411200000&isin=FR0000060832&mic=XPAR&dateFormat=d/m/Y&locale=null"
#precia 19/05
url3="https://www.euronext.com/sites/www.euronext.com/modules/common/common_listings/custom/nyx_eu_listings/nyx_eu_listings_price_chart/pricechart/pricechart.php?q=intraday_data&from=1495152000000&isin=FR0000060832&mic=XPAR&dateFormat=d/m/Y&locale=null"
historical = HistTransaction(url3)
historical.spiderData()"""