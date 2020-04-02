""" Load module: function to load json into mongo, to be called by extract scripts """
import pymongo

def to_mongo(data):
	conn = 'mongodb://localhost:27017'
	client = pymongo.MongoClient(conn)

	bazaarify = client.bazaarify

	collection = bazaarify.listings

	try:
		collection.insert_many(data)
		return True
	except Exception as a:
		return a
