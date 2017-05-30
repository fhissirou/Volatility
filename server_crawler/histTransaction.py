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

    def crawlHistTransEuronext(self):
        reponse = urllib.request.urlopen(self.getURLHISTTRANSACTION())
        body = reponse.read()
        strdata = body.decode("utf-8")
        try:
            self.setDATAHISTTRANSACTION(json.loads(strdata))
        except urllib2.HTTPError:
            pass

    #def crawlHistTransCAC40Boursorama(self):
