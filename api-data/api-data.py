from flask import Flask, request
import redis
from flask_cors import CORS, cross_origin



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

r = redis.Redis(host='172.25.1.134', port=6379, db=0)
ts = r.ts()

@app.route('/set', methods=['POST'])
def set():
    key = request.form['key']
    value = request.form['value']
    r.set(key, value)
    return f'Set {key} to {value}'

@app.route('/get', methods=['GET'])
def get():
    key = request.args.get('key')
    value = ts.range(key, 0, 9999999999999)
    a=[]
    for items in value:
        y="["+str(items[0])+","+str(items[1])+"]"
        a.append(y)
    return ','.join(a)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
