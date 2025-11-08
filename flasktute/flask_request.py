# using request() to retrive data from the webserver , request  is a class of flask module. we need to import request class to use request().
from flask import Flask, request,render_template
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def home():
    # return "WELCOME TO HOME PAGE "
    
    return render_template('index.html')

@app.route('/time')
def time():
    day_of_week=datetime.today().strftime('%A')
    mon=datetime.today().strftime('%B')
    yr=datetime.today().strftime('%Y')
    dt=datetime.today().strftime('%D')
    tm=datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, mon=mon, yr=yr, dt=dt, tm=tm)

@app.route('/add/<a>/<b>')
def addition(a,b):
    
    c=int(a)+int(b)
    print ("Addition of two integers",a, "and ", b, "is : ",c)
    result ={
        'addition':"Addition of two Numbers",
        'Values -1':a,
        'Value -2':b,   
        'ans':c
             }
    # l1=['value-1', 'value-2', 'addition of two numbers is']
    # l2=[a, b, c]
    return result
    
    # return "Addition of two numbers "+str(a)+" and "+str(b)+" is : "+str(c)

@app.route('/name/age')
def data():
    name=request.values.get('name')
    age=request.values.get('age')
    result={
        'Name':name,
        'Age':age
    }
    return result
    # return "Welcome to my website : "+name+" age "+age

if __name__=='__main__':
   app.run(debug=True)



