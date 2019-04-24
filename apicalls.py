import datetime
import requests
import json

def insert_log(payload):
    API_ENDPOINT = "http://127.0.0.1:5000/insert"
    API_KEY = "unknown key"

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    #print payload
    r = requests.post(url = API_ENDPOINT, json = payload, headers = headers)
    res = r.text
    sc = r.status_code
    print "Response is %s"%res
    print "Status Code is %s"%sc
    return sc     

def read_log():
    API_ENDPOINT = "http://127.0.0.1:5000/"
    API_KEY = "unknown key"

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.get(url = API_ENDPOINT, headers = headers)
    print r.json()
    sc = r.status_code
    return sc

def read_log_ts(ts1, ts2):
    API_ENDPOINT = "http://127.0.0.1:5000/getlog"
    API_KEY = "unknown key"
    params = {'ts1' : ts1, 'ts2': ts2}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.get(url = API_ENDPOINT, params = params, headers = headers)
    print r.json()
    sc = r.status_code
    return sc

if __name__ == "__main__":

    # An example of payload
    payload = {'log':{"time": "2010-01-01 00:00:00", "remote_ip": "93.180.71.3", "remote_user": "-", "request": "GET /downloads/product_1 HTTP/1.1", "response": 304, "bytes": 0, "referrer": "-", "agent": "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"}}
    print "Inserting the log, Status:%s"%insert_log(payload)
    print "Reading all the logs, Status:%s"%read_log()
