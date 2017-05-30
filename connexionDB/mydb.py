#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient


class MyDB(object):
	def __init__(self):
		pass

	def getConnection(self,host):
		try:
			retConnection = MongoClient(host)
		except Exception  as e:
			print("Exception occurred while creating connection with mongoDB, value: \n")
			print(e)
		return retConnection