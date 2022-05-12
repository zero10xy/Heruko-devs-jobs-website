from devs_for_hire_and_jobs_site import gMongoClient
from devs_for_hire_and_jobs_site.settings import MONGO_DB
import pymongo
from pymongo.server_api import ServerApi


def get_mongo_db(dbname="rum_data1"):
    # if dbname in gMongoClient:
    #     return gMongoClient[dbname]

    # if dbname in MONGO_DB:
    #with MONGO_DB[dbname] as config:
    	#gMongoClient = pymongo.MongoClient(config["CON_STR"],server_api=ServerApi('1'))
    # else:
    #     gMongoClient[dbname] = None

    return pymongo.MongoClient("mongodb+srv://rum:12345@cluster0.xtg4o.mongodb.net/rum_data1?retryWrites=true&w=majority",server_api=ServerApi('1'))[dbname]