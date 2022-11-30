from flask import Flask
from flask import request
import mysql.connector as mysql
import json as j
import time

# Maybe need to make a time.sleep here so the database has time to start

app = Flask(__name__)

connected = False
while not connected:
    try:
        db = mysql.connect(
            host="database",
            user="root",
            password="SAFECODE",
            database = "myDatabase",
            port = "3306"
        )
        connected = True
    except:
        print("Could not connect! Trying again in 5 seconds")
        time.sleep(5)


@app.route('/person', methods=['POST'])
def person():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    c = db.cursor()
    statement = """INSERT INTO persons(Firstname, Lastname) VALUES (%s, %s)"""
    values = (firstname, lastname)
    c.execute(statement, values)
    db.commit()
    return ("", 200)

@app.route('/persons', methods=['GET'])
def persons():
    c = db.cursor()
    c.execute("""SELECT * FROM persons""")
    result = c.fetchall()

    all_row_headers = []
    for i in c.description:
        all_row_headers.append(i[0])

    json_result = []
    for i in result:
        json_result.append(dict(zip(all_row_headers, i)))
    result_return = j.dumps(json_result)
    return (result_return, 200)

if __name__ == '__main__':
    app.run(host="0.0.0.0")