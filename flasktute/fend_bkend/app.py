# Data is fetched from front end through 'html forms' to backend i.e,Flask application.
# data fetched will not be stored as data base is not available.
# we use database like MongoDB, which is a NoSQL database and data is stored in documents in json format.

from flask import Flask, request,render_template
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

#----------------------------------------------------------------------------------------------------------------------------------------
#coping mongodb driver code and pasting it here, importing pymongo in flask application.

#uri = "mongodb+srv://dummy:1234@cluster0.q7mvh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(MONGO_URI)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# creating a data base with name 'test', we can give other names as well.
db =client.test
collection = db['flask-tutorial']

#----------------------------------------------------------------------------------------------------------------------------------------

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST','GET'])
def submit():
    # name= request.form.get('name')
    form_data=dict(request.form)
    # return 'Hello '+ name + '!, \nSignup is successful'
    # print(form_data)
    collection.insert_one(form_data)

    return "Submitted Data Successfull !!!!!y"

@app.route('/view')
def view():
    data=collection.find()
    data=list(data)

    for item in data:
     print(item)
    #return "Data Retrieved Successfully!!!!"
     del item['_id']

   
    
    return data

    

if __name__=='__main__':
    app.run(debug=True)