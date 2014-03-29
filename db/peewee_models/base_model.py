from peewee import *
import sqlite3

DB_PATH = '/home/karim/monakeb/db/khalil.db'
my_db = SqliteDatabase(DB_PATH)
# test_db = SqliteDatabase('test.db')
# test_2 = SqliteDatabase('new_db.db')

class BaseModel(Model):
    class Meta:
        database = my_db

# class TestModel(Model):
# 	class Meta:
# 		database = test_db

my_db.connect()