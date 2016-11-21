import flask
from flask import Flask
from flask import request
from parser import parse

app = Flask(__name__)

@app.route("/parse")
def handler():
    data = parse(request.args)
    if data:
    	return flask.jsonify( **data )
    else:
    	return "null"

if __name__ == "__main__":
	app.run(port=3000)