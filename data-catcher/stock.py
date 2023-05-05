import websocket
import time
import rel
import _thread as thread
import config
import json,redis, datetime
import requests_cache


REDIS_SERVER="172.25.1.134"
session = requests_cache.CachedSession('stock_cache',expire_after=3600)

def on_message(message):
    for item in message['Time Series (5min)'].keys():
        element=datetime.datetime.strptime(item,"%Y-%m-%d %H:%M:%S")
        timestamp = datetime.datetime.timestamp(element)
        ts.add('panw', int(timestamp)*1000,float(message['Time Series (5min)'][item]['1. open']))

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send(logon_msg)
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    r = redis.StrictRedis(host=REDIS_SERVER, port=6379, db=0)
    ts = r.ts()
    #ts.create('stock')
    response=session.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=PANW&interval=5min&outputsize=full&apikey=SOV0RIGV3FWV0SVR')
    on_message(json.loads(response.text))