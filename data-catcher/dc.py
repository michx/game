import websocket
import time
import rel
import _thread as thread
import config
import json,redis, datetime

REDIS_SERVER="172.25.1.134"


def on_message(ws, message):
    message=json.loads(message)
    ts.add('my_timeseries',int(datetime.datetime.timestamp(datetime.datetime.now())*1000) ,message["changes"][0][1])

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
    #ts.create('my_timeseries')
    logon_msg = '{"type": "subscribe","subscriptions":[{"name":"l2","symbols":["BTCEUR"]}]}'
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api.gemini.com/v2/marketdata/BTCEUR",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever (dispatcher=rel)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()