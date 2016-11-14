import flask
from flask import Flask
from flask import request
from parser import parse

app = Flask(__name__)


@app.route("/")
def handler():
    string = "hello I am a string and I know it!";
    # string = request.args.get("string")
    return flask.jsonify( **parse(string) )


if __name__ == "__main__":
	app.run()