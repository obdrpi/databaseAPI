# databaseAPI
A database API to fetch and insert logs in MYSQL

To run the code, please have all the dependencies installed such as Flask, Datetime, Requests etc.

SERVER:
To start the server, please run 'python main.py'
The server would listen on http://127.0.0.1:5000/ by default.

These are defined API endpoints:
POST: '/insert' 
Inserts a new log into the database and stores in JSON format.

GET: '/getlog'
Gets all the logs between two timestamps {timestamp1, timestamp2} from the table.

GET: '/'
Gets all the logs from the table.

On success, it would return 200 HTTP code whereas on failure, it would return 400 or 500 HTTP codes.

To hit the endpoints, please run these two python files:
- test_1.py : Contains the unit tests:
              1) Insert a log in JSON format with defined timestamp
              2) Insert a log in JSON format with absent timestamp (In this case, the database uses the then timestamp at insertion
              3) Gets all the logs between two given timestamps
              4) Inserts a string into the database
 
 - test_2.py : Contains the unit tests:
            1) Inserts all the logs from the file "nginx_json_logs.txt" in the database
            2) Gets all the logs from the database
            
            
            
 MySQL Database:
 We are using the "InnoDB" engine because it supports heavy insertions (since it locks only the row and not the whole table).
 To store the logs, we use two columns - log (JSON column) and ts (TIMESTAMP)
 
 1) We choose the 'schema-less' approach owing to the unpredictable structure and behavior of the logs in the future.
 2) The idea to use the JSON column is to incorporate the data from different and unknown sources. Also, the logs could change over time and this allows us to take care of those scenarios as well.
 3) We index the 'timestamp' column so as to query the logs faster using a range of timestamps
 4) All different queries for other JSON keys can be developed easily but obviously would not be equal in speed as indexing. This is a tradeoff between the speed and incorporating different types of log formats from unknown sources and hence we need to live with it.
 
