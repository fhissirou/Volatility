#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import json
import requests
import errno
from socket import error as SocketError


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
        reponse = requests.get(self.getURLHISTTRANSACTION(),verify=False)
        #reponse = urllib.request.urlopen(self.getURLHISTTRANSACTION())
        strdata = reponse.text
        #strdata = body.decode("utf-8")
        try:
            self.setDATAHISTTRANSACTION(json.loads(strdata))
        except urllib2.HTTPError, :
            pass
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                raise # Not error we are looking for
            pass # 

    #def crawlHistTransCAC40Boursorama(self):
