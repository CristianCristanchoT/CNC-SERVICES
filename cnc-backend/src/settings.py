import os
from pymongo import MongoClient

client = MongoClient(os.environ["DB_URL"])
#client = MongoClient('mongodb://admin:easydata@localhost:27017/CNC')

db = client['CNC']
preguntas = db['preguntas']