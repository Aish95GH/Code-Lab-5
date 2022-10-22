#!/usr/bin/python
from random import random
from flask import Flask, jsonify
import os
import random
import psycopg2
import json
  
# CREATE THE FLASK APP
app = Flask(__name__)
  
#establishing the connection
conn = psycopg2.connect( 
    database = os.environ.get('PG_DB'), #"db",
    user = os.environ.get('PG_USER'), #"root",
    password ='pass', #os.environ.get('PG_PASS'),
    host = os.environ.get('DB_HOST'),   #"db", 
    port = os.environ.get('PG_PORT')   #"5432" 
    )

#Executing an MYSQL function using the execute() method
@app.route('/')
@app.route('/',methods=[ 'GET',])
def index():
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    select_stmt = "SELECT MealName, MealPrice FROM Meals ORDER BY random() LIMIT 1"

    cursor.execute(select_stmt)
    """
    try:
        cursor.execute(select_stmt)
    except Exception as e:
        print(e.message)
        conn = psycopg2.connect( 
    database = os.environ.get('PG_DB'), 
    user = os.environ.get('PG_USER'),
    password ="pass",
    host = os.environ.get('DB_HOST'),
    port = os.environ.get('PG_PORT')
    )"""

#password = os.environ.get('PG_PASS')

    res =list(cursor.fetchone())
    
    return jsonify({res[0]:res[1]})
   

app.run('0.0.0.0',port=os.environ.get('API_PORT'),debug=True)
