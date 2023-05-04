from flask import Flask, request
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/set', methods=['POST'])
def set():
    key = request.form['key']
    value = request.form['value']
    r.set(key, value)
    return f'Set {key} to {value}'

@app.route('/get', methods=['GET'])
def get():
    key = request.args.get('key')
    value = r.get(key)
    return value