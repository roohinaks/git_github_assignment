from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask('__name__')
MONGO_URI= "mongodb+srv://dummy:1234@cluster0.q7mvh.mongodb.net/?appName=Cluster0"

client=MongoClient(MONGO_URI)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client["assignment"]
collection = db["flask-mongo"]

# ------------------------------------------------------------------------------------

app =Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html', error=None)

@app.route('/submit', methods=['GET','POST'])
def submit():
    name = request.form.get('name')
    phno = request.form.get('phno')
    address = request.form.get('address')
    card = request.form.get('card')
    expiry = request.form.get('expiry')
    cvv = request.form.get('cvv')

    print("Form Data:", request.form)

    if not name or not phno or not address or not card or not expiry or not cvv:
        return render_template('index.html', error="Error : All fields are mandatory")
    
    try:
        collection.insert_one({"name": name, "phno": phno, "address": address, "card": card, "expiry": expiry, "cvv": cvv})
        return redirect('/success')
    except Exception as e:
        return render_template('index.html', error=str(e))
    
@app.route('/success')
def success():
    return render_template('success.html')

if __name__=='__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
