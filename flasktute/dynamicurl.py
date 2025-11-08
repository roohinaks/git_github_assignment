from flask import Flask
#Creating a flask application instance
 
app=Flask(__name__)

#mapping url to specific function using decorator app.route('/')

#Decorator: 1
@app.route('/')
def home():
    return 'WELCOME TO HOME PAGE'

#Decorator: 2
@app.route('/name/<name>')
def name(name):
    print(name)
    return 'Welcome to NAME page'

#Decorator: 3
@app.route('/age/<age>')
def age(age):
    a=int(age)
    if a>=18:
        return 'you are eligible for VOTING'
    
    else:
        return 'you are too young for voting wait for some more years'
    
#Decorator: 4    
@app.route('/name/<name>/age/<age>')
def nameage(name,age):
    print(name)
    a=int(age)

    if a>=21 and a<=40:
        return 'You can marry'
    
    elif a<21:
        return f'You are too young to marry, wait for some more years'
    
    else:
        return 'Too old to marry, Pack your Bags'

#Decorator : 5
@app.route('/validation/name/<name>/age/<age>/perc/<perc>')
def validation(name,age,perc):
    length=len(name)
    print("number of characters in your name ",name," is : ", length)

    a=int(age)
    p=float(perc)

    if a>=22 and a<45:
        if p>=65:
            result= name + "!!!!!!   you are eligible to apply for post graduation"+"\n"+ "age is : " +str(a) +"\n"+ "percentage is : " + str(p)
            
            return result
        else:
            return "you are not eligible , because you have percentage below 65"
            
    elif a<22:
          return "complete your graduation"
    else:
        return "Try something else"

if __name__=='__main__':
    app.run(debug=True)

    
