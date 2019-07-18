"""This module is to configure app to connect with database."""

from pymongo import MongoClient

#DATABASE = MongoClient()['restfulapi-afarcloud'] # DB_NAME
DEBUG = True
SERVER_IP_PORT = MongoClient('mongo-db', 27017)
