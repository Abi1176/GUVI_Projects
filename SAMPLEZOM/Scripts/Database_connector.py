
import streamlit as st
import mysql.connector
from faker import Faker
import random

# Initialize Faker
fake = Faker()



class mySqlDBclass:
    def __init__(self,host,user,password,port,database):
      self.host=host
      self.user=user
      self.password=password
      self.port=port
      self.database=database
      self.conn=None
      self.cursor=None
      self.connect()
    def connect(self):
      self.conn=mysql.connector.connect(host=self.host,user=self.user,password=self.password,port=self.port,database=self.database)
      self.cursor=self.conn.cursor()
      print("DB Connection Successful!")
    def disconnect(self):
      if self.cursor:
        self.cursor.close()
        print("DB Connection Closed!")
    def create_table(self,table_query):
      self.cursor.execute(table_query)
      self.conn.commit()
      print(f"Table Created Successfully!")
    def insert_Values(self,insert_query,insertValues):
      self.cursor.executemany(insert_query,insertValues)
      self.conn.commit()
      print(f"Inserted Successfully!")

db_obj=mySqlDBclass.connect()
cursor=db_obj.cursor()

config = {"host":"gateway01.ap-southeast-1.prod.aws.tidbcloud.com", "user":"2B9qSGSxQso7gBp.root", "port":4000, "password":"nLUDS0fz3HRQatbm", "database":"MONK"}
db_obj = mySqlDBclass(**config)
