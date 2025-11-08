from flask import Flask,jsonify,request,render_template
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
URI=os.getenv('MONGO_URI')

client=MongoClient(URI)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client.assignment
collection=db.form_collection

app=Flask(__name__)

@app.route('/')
def home():

    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    data=dict(request.form)
    collection.insert_one(data)
    return jsonify({"status":"success", "message":"Data inserted successfully", "data":data})

@app.route('/view')
def view():
    data=collection.find()
    for item in data:
        print(item)
        del item['_id']

    data={
            'data':data
        }
    return data

if __name__=='__main__':
    app.run(debug=True)

