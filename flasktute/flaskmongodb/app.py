from flask import Flask,jsonify
import json

app=Flask(__name__)

def read_data():
    with open("json_data.json","r") as file:
        return json.load(file)




@app.route('/api', methods=['GET'])
def api():
    try:
        data=read_data()
        return jsonify({"Status":"successful","data":data}),200
    except Exception as e:
        return jsonify({"Status":"error", "message":str(e)}),500
    
    
if __name__=='__main__':
     app.run(debug=True)
       




