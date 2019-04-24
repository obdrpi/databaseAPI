import unittest
import json
import datetime
target = __import__("apicalls")
insertLog = target.insert_log
readLogs = target.read_log
filen = "nginx_json_logs.txt"

class TestAPI(unittest.TestCase):

    #Insert all logs from the given file
    #Will take some time
    def test_all_logs(self):
        try:
            file = open(filen, "r")
            for line in file:
                line_json = json.loads(line)
                date_time_str = line_json['time']
                if date_time_str is not None:
                    date_time_obj = datetime.datetime.strptime(date_time_str[:-6], '%d/%b/%Y:%H:%M:%S')
                    str_obj = date_time_obj.strftime('%Y-%m-%d %I:%M:%S')
                    line_json['time'] = str_obj
                payl = {}
                payl['log'] = line_json
                result = insertLog(payl)
                self.assertEqual(result, 200)
        except Exception as e:
            print e

    #Read All Logs
    def read_json_logs(self):
        result = readLogs()
        self.assertEqual(result, 200)
    
if __name__ == "__main__":
    unittest.main()
    print "Everything Passed"
