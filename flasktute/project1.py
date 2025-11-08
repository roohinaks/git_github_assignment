from flask import Flask,render_template
from datetime import datetime

app=Flask(__name__)

@app.route('/<name>')
def welcome(name):

    return render_template('project1.html', name=name)

@app.route('/index')
def index():
    day_of_week=datetime.today().strftime('%A')
    mon=datetime.today().strftime('%B')
    yr=datetime.today().strftime('%Y')
    dt=datetime.today().strftime('%D')
    tm=datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, mon=mon, yr=yr, dt=dt, tm=tm)

@app.route('/home')
def home():
    return render_template('home.html')

    

if __name__=='__main__':
   app.run(debug=True)
