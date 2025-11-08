from flask import Flask,render_template,request
import requests
import json


BACKEND_URL='http://0.0.0.0:9000'+'/submit'

app=Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    form_data=dict(request.form)
    print(form_data)
    headers={'Content-Type':'application/json'}

    requests.post(BACKEND_URL,headers=headers, json = form_data)
   

    return "Data sent Successfully!!!!!!!"


if __name__=='__main__':
    app.run(debug=True)
