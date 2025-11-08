# installing Flask command: pip3 install Flask.
# importing Flask to this class
from flask import Flask

#Creating  Flask Application instance (Flask('__name__')) and assigning instance to an variable 'app', instance is a String
app = Flask('__name__')

#Creating webpage of app using route(/path)
#@app.route() is a decorator which map URL route / to that function.
#Note: for the same function we can map multiple decorators.
@app.route('/')
@app.route('/home')
def home():
   
    return "Welcome to home page!!!!!!!!!"

# using route to create subpages
@app.route('/zip/<name>')
def zip(name):

    print(name)

    return "welcome to signup page "



if (__name__=='__main__'):
    app.run(debug=True)


