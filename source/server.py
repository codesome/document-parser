from flask import Flask,request,jsonify
from parser import *

app = Flask(__name__)

@app.route("/parse")
def parse_handler():
    data = parse(request.args)
    if data:
    	return jsonify( **data )
    else:
    	return "null"

@app.route("/topics")
def topic_handler():
    data = topics(request.args.get("str"))
    if data:
	    return jsonify( **data )
    else:
    	return "null"

if __name__ == "__main__":
	app.run(port=3000)