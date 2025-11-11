from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient

MONGO_URI= "mongodb+srv://dummy:1234@cluster0.q7mvh.mongodb.net/?appName=Cluster0"
client=MongoClient(MONGO_URI)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db=client["git"]
collection = db["todoitem"]
# -----------------------------------------------------------------------------------
app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submittodoitem', methods=['POST'])
def submit():
    itemname=request.form.get('itemname')
    description=request.form.get('description')

    print("Form Data:", request.form)

    item= {"name": itemname, "description": description}
    collection.insert_one(item)

    return render_template('index.html', message="Item added successfully")

if __name__=='__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
