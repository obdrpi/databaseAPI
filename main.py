import pymysql
from app import app
from flask import Flask, flash, render_template, request, redirect, jsonify
from config_db import mysql
from showdict import Results
from werkzeug import generate_password_hash, check_password_hash
import json

@app.route('/insert', methods=['POST'])
def insert_log():
    try:
        log = request.get_json()
        logv = log["log"]
        if logv and request.method == 'POST':
            try:
                sql = "insert into jsonlogs (log) VALUES (%s)"
                values = json.dumps(logv)
                conn = mysql.connect()
                cur = conn.cursor()
                cur.execute(sql, values)
                conn.commit()
                return "Log Addition Successful!", 200
            except Exception as e:
                return "Insertion Failed!", 500
            finally:
                cur.close()
                conn.close()
        else:
            return "Empty Log!", 400
    except Exception as e:
        return "Bad request!", 400

@app.route('/getlog', methods=['GET'])
def read_log():
    try:
        ts1 = request.args.get('ts1')
        ts2 = request.args.get('ts2')
        print ts1
        print ts2
        conn = mysql.connect()
        cur = conn.cursor()
        sql = "select * from jsonlogs where ts between %s and %s"
        values = (ts1,ts2,)
        cur.execute(sql, values)
        rows = cur.fetchall()
        return jsonify(rows), 200
    except Exception as e:
        return "Bad Request", 400
    finally:
        cur.close()
        conn.close()


@app.route('/')
def read_logs():
    try:
        conn = mysql.connect()
        cur = conn.cursor()
        sql = "select log from jsonlogs"
        cur.execute(sql)
        rows = cur.fetchall()
        return jsonify(rows), 200
    except Exception as e:
        return "Bad Request", 400 
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    app.run()

