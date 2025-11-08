from flask import Flask, jsonify
from list import get_data

app = Flask('__name__')

@app.route('/api', methods=['GET'])
def api():
    list=get_data()
    list= {
        'LIST OF AWS SERVICES' : list
    }
    
    return jsonify(list)

if __name__=='__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')