from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


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
        app.logger.info(request.data)
        return request.data
    else:
        page = dict({"title" : "Hello World"})
        return render_template('ajax.html', page=page)


@app.route("/hello/<string:name>/")
def getMember(name):
    page = dict({"title" : "Hello " + name,
                 "content" : "kgsfdfg g dfsg fds gdfsgsdg dfg dfsg fdg s",
                 "records" : [a for a in range(5)]})
    return render_template('test.html', page=page)


if __name__ == "__main__":
    app.debug = True
    app.run()
