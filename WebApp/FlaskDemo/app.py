from flask import Flask, render_template, request, jsonify
import sqlite3
import json

app = Flask(__name__)
conn = {}

@app.route("/")
def index():
    page = dict({"title" : "Index"})
    return render_template('test.html', page=page)


@app.route("/hello")
def hello():
    page = dict({"title" : "Hello World"})
    return render_template('test.html', page=page)


@app.route("/ajax", methods=["GET", "POST"])
def load_ajax():
    if request.method == "POST":
        app.logger.info(json.loads(request.data)[0])
        if json.loads(request.data)[0]["delete"]:
            deleteUser(json.loads(request.data)[0]["User"]["name"])
        else:
            insertUser(json.loads(request.data)[0]["User"]["name"])
        return request.data
    else:
        page = dict({"records" : getUsers()})
        return render_template('ajax.html', page=page)


@app.route("/hello/<string:name>/")
def getMember(name):
    page = dict({"title" : "Hello " + name,
                 "content" : "kgsfdfg g dfsg fds gdfsgsdg dfg dfsg fdg s",
                 "records" : [a for a in range(5)]})
    return render_template('test.html', page=page)

def initDataSource():
    conn = sqlite3.connect('databsae.db')
    print "Opened database successfully";
    try:
        conn.execute('CREATE TABLE User (id INTEGER PRIMARY KEY, name TEXT)')
        print "Table created successfully";
    except Exception, e:
        print e
    conn.close()


def insertUser(name):
    with sqlite3.connect("databsae.db") as con:
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO User (name) VALUES (?)", (name,))
            con.commit()
            print "Record successfully added"
        except Exception, e:
            con.rollback()
            print e
            print "error in insert operation"


def deleteUser(name):
    with sqlite3.connect("databsae.db") as con:
        cur = con.cursor()
        print name
        try:
            cur.execute("DELETE FROM User WHERE name IN (?)", (name,))
            con.commit()
            print "Record successfully deleted"
        except Exception, e:
            con.rollback()
            print e
            print "error in delete operation"


def getUsers():
    with sqlite3.connect("databsae.db") as con:
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("select * from User")

        rows = cur.fetchall();
        return rows

if __name__ == "__main__":
    #initDataSource()
    app.debug = True
    app.run()
    #insertUser("dadasddsa")
    #insertUser("dadasddsa")
    #insertUser("dadasddsa")
    #insertUser("dadasddsa")
    #print getUsers()

    #print len(getUsers())
    #deleteUser("FSDAFDSA")
    #print len(getUsers())