#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import json
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
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

        req = urllib.request.Request(self.getURLHISTTRANSACTION(),headers = headers)
        reponse = urllib.request.urlopen(req)
        #strdata = reponse.text
        body= reponse.read()
        strdata = body.decode("utf-8")
        try:
            self.setDATAHISTTRANSACTION(json.loads(strdata))
        except urllib2.HTTPError:
            pass
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                raise # Not error we are looking for
            pass # 

    #def crawlHistTransCAC40Boursorama(self):
