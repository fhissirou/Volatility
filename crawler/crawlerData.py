#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import bs4
import re
import urllib.request
import json
import operator
import datetime
import time
from carnetOrdres import CarnetOrdres
from  histTransaction import HistTransaction
from pymongo import MongoClient

class CrawlerData(CarnetOrdres, HistTransaction):
    def __init__(self):
        CarnetOrdres.__init__(self)
        HistTransaction.__init__(self)
        self.MONGOCLIENT= MongoClient('mongodb://localhost:27017/')
        self.DB= self.MONGOCLIENT["Volatility"]
    
    def crawlAllHist(self):
        collection= self.DB["actions_europeennes"].find({})
        compt=1
        for obj in collection:
            _nom = str(obj["Nom"])
            _isin= str(obj["Isin"])
            _mic= str(obj["Mic"])
            print(str(compt)+"- Nom: "+_nom+" , ISIN: "+_isin+"-"+_mic)
            self.findDataHistEuronnext(_nom,_isin,_mic)
            time.sleep(3)
            compt+=1

    def getAllAction(self):
        actions= self.DB["actions_europeennes"]
        self.EUROACTIONS= actions.find({},{"_id":0, "Capitaux":0})

    def genUrlHistEuronext(self,_isin, _mic):
        date_time = time.strftime("%d/%m/%Y")
        date_time+=" 02:00:00"
        pattern = "%d/%m/%Y %H:%M:%S"
        today= int(time.mktime(time.strptime(date_time, pattern)))
        strtoday= str(today)+"000"
        
        url = "https://www.euronext.com/sites/www.euronext.com/modules/common/common_listings/custom/nyx_eu_listings/nyx_eu_listings_price_chart/pricechart/pricechart.php?q=intraday_data"
        url+="&from="+strtoday
        url+="&isin="+str(_isin)
        url+="&mic="+str(_mic)
        url+="&dateFormat=d/m/Y&locale=null"
        
        return url

    def verif_first_use(self, _id):
        collection=  self.DB["historiques_transactions"]
        if collection.find({"_id":_id}).count() > 0:
            return -1
        else: 
            return 1

    def findDataHistEuronnext(self,_nom,_isin,_mic):
        dictionnaire= {}
        historique={}
        ldic=[]
        now = datetime.datetime.now()
        dt_time= now.strftime("%Y-%m-%d %H:%M")
        collection= self.DB["historiques_transactions"]
        idname=str(_nom+"_"+str(_isin)+"-"+str(_mic))
        url = self.genUrlHistEuronext(_isin,_mic)
        self.setURLHISTTRANSACTION(url)
        self.crawlDataHistTransaction()
        data = self.getDATAHISTTRANSACTION()

        if len(data) > 0:
            
            dt= data["data"]
            dt.sort(key=operator.itemgetter("tradeId"))
            
            for elem in dt:
                dic={}
                dic["TradeId"]=elem["tradeId"]
                dic["DateAndTime"]= elem["dateAndTime"]
                dic["TimeZone"]= elem["timeZone"]
                dic["Price"]= elem["price"]
                dic["NumberOfShares"]= elem["numberOfShares"]
                dic["TRADE_QUALIFIER"]= elem["TRADE_QUALIFIER"]
                ldic.append(dic)
            
            historique[str(dt_time)]=ldic
            first= self.verif_first_use(idname)
            
            if first == 1:
                dictionnaire["_id"]= idname
                dictionnaire["Nom"]=_nom
                dictionnaire["Isin"]=_isin
                dictionnaire["Mic"]=_mic
                dictionnaire["Historiques"]=historique
                #insertion dans la base de donnée
                document={}
                document[str(_nom+"_"+str(_isin)+"-"+str(_mic))]=dictionnaire
                collection.insert(dictionnaire)
            
            else:
                strhist=idname+".Historiques"
                document= collection.update({"_id":idname},\
                    {"$set":{"Historiques"+"."+str(dt_time):historique[str(dt_time)]}})

        else:
            print("Error de récupération sur Nom: "+_nom+" , ISIN: "+_isin+"-"+_mic)
            pass

# 22/05
url1="https://www.euronext.com/sites/www.euronext.com/modules/common/common_listings/custom/nyx_eu_listings/nyx_eu_listings_price_chart/pricechart/pricechart.php?q=intraday_data&from=1495411200000&isin=FR0011584549&mic=XPAR&dateFormat=d/m/Y&locale=null"

#precia 19/05
url2="https://www.euronext.com/sites/www.euronext.com/modules/common/common_listings/custom/nyx_eu_listings/nyx_eu_listings_price_chart/pricechart/pricechart.php?q=intraday_data&from=1495152000000&isin=FR0000060832&mic=XPAR&dateFormat=d/m/Y&locale=null"

#precia 18/05
url4="https://www.euronext.com/sites/www.euronext.com/modules/common/common_listings/custom/nyx_eu_listings/nyx_eu_listings_price_chart/pricechart/pricechart.php?q=intraday_data&from=1000&isin=FR0000060832&mic=XPAR&dateFormat=d/m/Y&locale=null"


crawl = CrawlerData()
crawl.crawlAllHist()