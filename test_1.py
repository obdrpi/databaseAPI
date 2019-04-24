import unittest
import json
import datetime
target = __import__("apicalls")
insertLog = target.insert_log
readLog = target.read_log_ts

class TestAPI(unittest.TestCase):
    #Correct Payload with needed timestamp
    def test_json_log1(self):
        payload = {'log':{"time": "2010-01-01 00:00:00", "remote_ip": "93.180.71.3", "remote_user": "-", "request": "GET /downloads/product_1 HTTP/1.1", "response": 304, "bytes": 0, "referrer": "-", "agent": "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"}}
        result = insertLog(payload)
        self.assertEqual(result, 200)

    
    def test_json_log2(self):
        #Payload with missing timestamp
        #Record will be inserted with the current time stamp
        payload = {'log':{"remote_ip": "93.180.71.3", "remote_user": "-", "request": "GET /downloads/product_1 HTTP/1.1", "response": 304, "bytes": 0, "referrer": "-", "agent": "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"}}
        #print type(payload)
        result = insertLog(payload)
        self.assertEqual(result, 200)

    def test_json_log3(self):
        timestamp1 = "2015-05-17 03:05:09"
        timestamp2 = "2015-05-17 03:05:37"
        result = readLog(timestamp1, timestamp2)
        self.assertEqual(result, 200)

if __name__ == "__main__":
    unittest.main()
    print "Everything Passed"
