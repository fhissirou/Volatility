#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient

class MongoDBConnection():
	def __init__(self):
		pass

	def getConnection(self,host):
		try:
			retConnection = MongoClient(host)
		except Exception  as e:
			print("Exception occurred while creating connection with mongoDB, value: \n")
			print(e)
		return retConnection

	def showAllRecords(self,host,db,collection):
		#pdb.set_trace()
		hconn = self.getConnection(host)
		hdb = self.getDBDetails(hconn,'test')
		hcoll = self.getCollectionDetails(hdb,'documents')

		#get all the details about the collection
		query = {"name" : "SP"}
		try:
			cursor = hcoll.find(query)
		except Exception as e:
			print "Unexpected error:", type(e), e
		return cursor

	def getDBDetails(self,connection,db):
		# create a database connection
		try :
			retDb = connection[db] # NOTE : dictionary style access
		except Exception as e:
			print 'Exception occurred while connecting to database %s, value: \n ' % db
			print e
		return retDb

	def getCollectionDetails(self,db,collection):
		#create a handle for collection
		try :
			retCollection = db[collection] # NOTE : dictionary style access
		except Exception as e:
			print 'Exception occurred while getting details for  collection:  %s, value: \n ' % collection
			print e
		return retCollection