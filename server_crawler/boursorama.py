#!/usr/bin/env python
# -*- coding: utf-8 -*-

#http://www.boursorama.com/bourse/cours/includes/last_transactions.phtml?symbole=1rPCAC

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

class CrawlerBoursorama(CarnetOrdres, HistTransaction):
    def __init__(self):
        CarnetOrdres.__init__(self)
        HistTransaction.__init__(self)
        self.MONGOCLIENT= MongoClient('mongodb://localhost:27017/')
        self.DB= self.MONGOCLIENT["Volatility"]
        self.now = datetime.datetime.now()

    def verif_first_use(self, _id):
        collection=  self.DB["cac40"]
        if collection.find({"_id":_id}).count() > 0:
            return -1
        else: 
            return 1

    def crawlCAC40(self):
        dbcac40= self.DB["cac40"]
        dt_time= self.now.strftime("%Y-%m-%d %H:%M")
        url=""
        if self.verif_first_use("CAC40") == -1:
            collection = dbcac40.find({"_id":"CAC40"},{"_id":0, "Url":1})
            for obj in collection:
                url = str(obj["Url"])

            doc = self.findDataCAC40(url)
            if len(doc) > 0:
                dbcac40.update({"_id": "CAC40" },{ "$set": doc})


    def findDataCAC40(self, url):
        dictionnaire={}
        ldic=[]
        dt_time= self.now.strftime("%Y-%m-%d %H:%M")
        with urllib.request.urlopen(url) as f:
            data = f.read()#.decode('utf-8')
            soup = bs4.BeautifulSoup(data, 'html.parser')
            tbody = soup.find('tbody')
            for tr in tbody.find_all('tr'):
                num_column=0
                dic={}
                for td in tr.find_all('td'):
                    if num_column == 0:
                        dic["Heures"]= str(td.get_text('', strip=True))
                    if num_column == 1:
                        dic["Cours"]= str(td.get_text('', strip=True))
                    num_column+=1

                if len(dic) > 0:
                    ldic.append(dic)

            if len(ldic) > 0:
                dictionnaire[str(dt_time)]= ldic
        return dictionnaire



crawl = CrawlerBoursorama()
crawl.crawlCAC40()