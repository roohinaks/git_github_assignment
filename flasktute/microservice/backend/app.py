from flask import Flask,request,render_template,jsonify
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
import json


BACKEND_URL='http://0.0.0.0:9000'


load_dotenv()
URI=os.getenv('MONGO_URI')


#---------------------------------------------------------------------------------------------------------------------

# Create a new client and connect to the server
client = MongoClient(URI)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#creating a data base with name microservice in mongodb server. create a collection inside db.
db=client.microservice

collection=db['micro-tute']

#---------------------------------------------------------------------------------------------------------------------------
app=Flask(__name__)

@app.route('/submit', methods=['GET','POST'])
def submit():
    # form_data=dict(request.args.get(json))
    data=request.json
    collection.insert_one(data)

    return "Sucessfully submitted Form !!!!!!"

@app.route('/view')
def view():
    data=collection.find()
    data=list(data)

    for item in data:
        print(item)
        del item['_id']

    
    return data

if __name__=='__main__':
    app.run(host='0.0.0.0',port='9000',debug=True)